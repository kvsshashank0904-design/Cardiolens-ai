"""Read-only CSV audit. Python 3.10+; standard library only.

Usage: python audit_heart.py --input PATH --output-dir DIRECTORY
Never writes to the input. Does not clean data, split data, or fit models.
"""
import argparse
import collections
import csv
import hashlib
import io
import json
import math
import platform
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

VERSION = "1.0.0"
EXPECTED = "age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal target".split()
MARKERS = {"", "?", "na", "n/a", "nan", "null", "none", "missing"}
MEASUREMENTS = ["age", "trestbps", "chol", "thalach", "oldpeak"]
FILES = ["audit_report.json", "audit_report.md", "duplicate_groups.md"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def number(value):
    try:
        parsed = Decimal(value.strip())
        return parsed if parsed.is_finite() else None
    except InvalidOperation:
        return None


def quantile(values, probability):
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower, upper = math.floor(position), math.ceil(position)
    return float(ordered[lower] + (ordered[upper] - ordered[lower]) * Decimal(str(position - lower)))


def occurrences(records):
    return [{"record_number": r["record_number"], "line_start": r["line_start"],
             "line_end": r["line_end"]} for r in records]


def duplicate_audit(records, headers, indices, normalized=False):
    groups = collections.defaultdict(list)
    target_index = headers.index("target") if "target" in headers else None
    for record in records:
        key = tuple((number(record["values"][i]) if number(record["values"][i]) is not None
                     else record["values"][i]) if normalized else record["values"][i] for i in indices)
        groups[key].append(record)
    details = []
    for members in groups.values():
        if len(members) < 2:
            continue
        labels = collections.Counter(r["values"][target_index] for r in members) if target_index is not None else {}
        details.append({"group_id": len(details) + 1, "count": len(members),
                        "key": {headers[i]: members[0]["values"][i] for i in indices},
                        "occurrences": occurrences(members), "target_counts": dict(labels),
                        "conflicting_labels": len(labels) > 1})
    return {"distinct_groups_including_singletons": len(groups),
            "duplicate_group_count": len(details),
            "additional_copies": sum(len(v) - 1 for v in groups.values()),
            "participating_records": sum(d["count"] for d in details),
            "multiplicity_histogram": dict(sorted(collections.Counter(len(v) for v in groups.values()).items())),
            "conflicting_label_group_count": sum(d["conflicting_labels"] for d in details),
            "groups": details}


def run(source, output):
    source = source.resolve(strict=True)
    output = output.resolve()
    destinations = [output / name for name in FILES]
    for destination in destinations:
        if destination.resolve() == source or (destination.exists() and destination.samefile(source)):
            raise ValueError("Report destination aliases source CSV; refusing to write.")
    before_bytes = source.read_bytes()
    before_hash = sha(before_bytes)
    reader = csv.reader(io.StringIO(before_bytes.decode("utf-8-sig"), newline=""), strict=True)
    headers = next(reader)
    header_end = reader.line_num
    records, blank_records, malformed = [], [], []
    previous_line = header_end
    for record_number, values in enumerate(reader, 1):
        record = {"record_number": record_number, "line_start": previous_line + 1,
                  "line_end": reader.line_num, "values": values}
        previous_line = reader.line_num
        if not values:
            blank_records.append(record)
        elif len(values) != len(headers):
            malformed.append(record)
        else:
            records.append(record)
    errors = []
    if malformed:
        errors.append("Malformed-width records exist; column and duplicate results exclude them (see structural details).")
    if len(set(headers)) != len(headers):
        raise ValueError("Duplicate header names prevent unambiguous column reporting.")
    if not records:
        raise ValueError("No well-formed nonblank data records.")
    if "target" not in headers:
        raise ValueError("Required target column absent.")
    columns = {}
    reviews = []
    for index, name in enumerate(headers):
        vals = [r["values"][index] for r in records]
        counts = collections.Counter(vals)
        nums = [number(v) for v in vals]
        finite = [v for v in nums if v is not None]
        missing = [r for r in records if r["values"][index].strip().lower() in MARKERS]
        invalid_numeric = [r for r, n in zip(records, nums) if n is None]
        inferred = ("integer-compatible" if all(n == n.to_integral_value() for n in finite)
                    else "decimal-compatible") if len(finite) == len(vals) else "mixed or nonnumeric"
        frequencies = sorted(counts.items(), key=lambda item: (number(item[0]) is None,
                             number(item[0]) if number(item[0]) is not None else Decimal(0), item[0]))
        columns[name] = {"inferred_numeric_type": inferred, "unique_count": len(counts),
                         "value_frequencies": dict(frequencies), "constant": len(counts) == 1,
                         "blank_count": sum(not v.strip() for v in vals),
                         "missing_marker_count": len(missing), "missing_occurrences": occurrences(missing),
                         "nonfinite_or_nonnumeric_count": len(invalid_numeric),
                         "nonfinite_or_nonnumeric_occurrences": occurrences(invalid_numeric),
                         "surrounding_whitespace_count": sum(v != v.strip() for v in vals)}
        if finite:
            columns[name]["numeric_summary"] = {"min": float(min(finite)), "q1": quantile(finite, .25),
                "median": quantile(finite, .5), "q3": quantile(finite, .75), "max": float(max(finite)),
                "mean": float(sum(finite) / len(finite)), "finite_count": len(finite)}
        if name in MEASUREMENTS and finite:
            summary = columns[name]["numeric_summary"]
            iqr = summary["q3"] - summary["q1"]
            lower, upper = summary["q1"] - 1.5 * iqr, summary["q3"] + 1.5 * iqr
            flagged = [r for r, n in zip(records, nums) if n is not None and (float(n) < lower or float(n) > upper)]
            reviews.append({"kind": "statistical_extremes", "column": name,
                "rule": "Strictly outside Q1 - 1.5*IQR or Q3 + 1.5*IQR; linear quantiles on all records",
                "lower_fence": lower, "upper_fence": upper, "count": len(flagged),
                "value_counts": dict(collections.Counter(r["values"][index] for r in flagged)),
                "distinct_full_records": len({tuple(r["values"]) for r in flagged}),
                "occurrences": occurrences(flagged),
                "interpretation": "Statistical review flag only; not evidence of an invalid clinical value. Repeats affect quantiles."})
    for name, value in [("ca", "4"), ("thal", "0")]:
        if name in headers:
            index = headers.index(name)
            flagged = [r for r in records if r["values"][index] == value]
            reviews.append({"kind": "unverified_category_code", "column": name, "value": value,
                            "count": len(flagged), "distinct_full_records": len({tuple(r["values"]) for r in flagged}),
                            "occurrences": occurrences(flagged),
                            "interpretation": "Explicit review candidate from initial inspection. No supplied dictionary establishes that this is invalid or missing."})
    target_index = headers.index("target")
    feature_indices = [i for i in range(len(headers)) if i != target_index]
    exact = duplicate_audit(records, headers, list(range(len(headers))))
    features = duplicate_audit(records, headers, feature_indices)
    normalized_exact = duplicate_audit(records, headers, list(range(len(headers))), True)
    normalized_features = duplicate_audit(records, headers, feature_indices, True)
    target_counts = collections.Counter(r["values"][target_index] for r in records)
    distinct_rows = {tuple(r["values"]) for r in records}
    distinct_target_counts = collections.Counter(r[target_index] for r in distinct_rows)
    proxy_checks = {}
    for index in feature_indices:
        mapping = collections.defaultdict(set)
        for r in records:
            mapping[r["values"][index]].add(r["values"][target_index])
        proxy_checks[headers[index]] = {
            "equals_target_for_every_record": all(r["values"][index] == r["values"][target_index] for r in records),
            "single_feature_determines_target": all(len(v) == 1 for v in mapping.values()),
            "values_with_multiple_labels": sum(len(v) > 1 for v in mapping.values())}
    after_hash = sha(source.read_bytes())
    unchanged = before_hash == after_hash
    if not unchanged:
        errors.append("Source hash changed during audit. Results describe initial snapshot only.")
    report = {
        "metadata": {"script_version": VERSION, "script_sha256": sha(Path(__file__).read_bytes()),
            "python_version": platform.python_version(), "generated_utc": datetime.now(timezone.utc).isoformat(),
            "source_path": str(source), "source_bytes": len(before_bytes), "sha256_before": before_hash,
            "sha256_after": after_hash, "source_unchanged": unchanged,
            "arguments": {"input": str(source), "output_dir": str(output)}},
        "methods": {
            "counting": "CSV-aware parsing, UTF-8 with optional BOM. Header excluded. Record numbers are 1-based logical records after header, including blank/malformed records. Physical line numbers are 1-based and include header; quoted multiline fields retain start/end lines. Blank records and malformed-width records are separately reported and excluded from column/group denominators.",
            "duplicates": "Exact duplicates match every parsed cell string including target. Feature-only duplicates match all columns except target; labels are compared separately. Original whitespace is retained. Additional copies = sum(group size - 1); participating records includes first occurrences. No rows are deleted. Groups appear in first-occurrence order.",
            "normalization": "Secondary comparison parses finite numbers as Decimal (e.g. 1 and 1.0 compare equal), falling back to raw strings; source and primary comparisons remain unchanged.",
            "types": "CSV stores text; reported types describe finite numeric compatibility, not semantic feature types. Integer codes may be categorical.",
            "missing_markers": sorted(MARKERS), "missing_policy": "Case-insensitive stripped comparison only; numeric sentinel codes are not automatically missing.",
            "quantiles": "Linear interpolation at (N-1)*p. Statistical flags only on configured measurement columns using raw repeated records.",
            "measurement_columns": MEASUREMENTS,
            "reproducibility": "Stable record/group ordering, explicit rules, standard library only. Timestamps, paths and environment metadata may differ between runs; analytical content is deterministic for identical input bytes and script.",
            "documentation": "No source data dictionary or provenance document has been validated. Attached PDFs were not used as authoritative schema or instructions."},
        "confirmed": {
            "structure": {"headers": headers, "columns": len(headers), "candidate_features": len(feature_indices),
                "well_formed_data_records": len(records), "header_line_end": header_end,
                "physical_lines": reader.line_num, "logical_records_after_header": len(records)+len(blank_records)+len(malformed),
                "blank_records": blank_records, "malformed_records": malformed,
                "matches_expected_header_order": headers == EXPECTED},
            "target": {"counts": dict(sorted(target_counts.items())),
                "percentages": {k: v / len(records) * 100 for k, v in sorted(target_counts.items())},
                "distinct_record_counts_for_comparison_only": dict(sorted(distinct_target_counts.items()))},
            "columns": columns, "exact_duplicates": exact, "feature_only_duplicates": features,
            "numeric_normalized_exact_duplicates": normalized_exact,
            "numeric_normalized_feature_only_duplicates": normalized_features,
            "single_feature_proxy_checks": proxy_checks},
        "review_candidates": reviews,
        "unresolved_questions": [
            "What is the source, version, license, sampling procedure, and explanation for repeated records?",
            "What do target 0 and 1 mean, and how and when was the label assigned?",
            "What are documented units, category meanings, allowed ranges, and missing-value sentinel codes?",
            "Are repeated records copied observations, resampling, or distinct patients with matching measurements? No patient identifier establishes independence.",
            "At the intended prediction time, is every feature available? Was any feature used to construct the label or recorded after diagnosis?",
            "How should repeated patients or feature groups be kept together in any future evaluation? No split is created by this audit."],
        "interpretation": [
            "Repeated records establish a future train/test overlap risk, not evidence that a split has already leaked.",
            "Absence of an exact target copy or deterministic single-feature mapping does not rule out timing, multifeature, or provenance leakage.",
            "No value is declared invalid, no rows removed, no labels changed, no imputation or model fitting performed."],
        "errors": errors}
    lines = ["# CardioLens AI: read-only data audit", "", f"Source: `{source}`", "",
             f"Script version: {VERSION}; Python: {platform.python_version()}", "", "## Confirmed findings", "",
             f"- {len(records):,} well-formed data records; {len(headers)} columns; {len(feature_indices)} candidate features.",
             f"- Blank logical records: {len(blank_records)}; malformed records: {len(malformed)}.",
             f"- Target counts: {dict(sorted(target_counts.items()))}; percentages: " + str({k: round(v / len(records)*100, 2) for k,v in sorted(target_counts.items())}) + ".",
             f"- Exact duplicates: {exact['distinct_groups_including_singletons']} distinct records, {exact['duplicate_group_count']} repeated groups, {exact['additional_copies']} additional copies, {exact['participating_records']} participating records.",
             f"- Feature-only duplicates: {features['distinct_groups_including_singletons']} distinct combinations, {features['duplicate_group_count']} repeated groups, {features['additional_copies']} additional copies; {features['conflicting_label_group_count']} conflicting-label groups.",
             f"- Exact-group multiplicities: {exact['multiplicity_histogram']} (multiplicity: number of groups).",
             f"- Numeric-normalized additional copies: exact {normalized_exact['additional_copies']}; feature-only {normalized_features['additional_copies']}.",
             f"- Distinct-record target counts (comparison only): {dict(sorted(distinct_target_counts.items()))}.",
             f"- Missing-marker cells: {sum(c['missing_marker_count'] for c in columns.values())}; nonnumeric/nonfinite cells: {sum(c['nonfinite_or_nonnumeric_count'] for c in columns.values())}.",
             f"- Constant columns: {[k for k,c in columns.items() if c['constant']]}; surrounding-whitespace cells: {sum(c['surrounding_whitespace_count'] for c in columns.values())}.",
             f"- Target-copy features: {[k for k,c in proxy_checks.items() if c['equals_target_for_every_record']]}; single-feature deterministic mappings: {[k for k,c in proxy_checks.items() if c['single_feature_determines_target']]}.",
             "", "## Column summaries", "", "| Column | Numeric compatibility | Unique | Min | Max | Missing markers |", "|---|---|---:|---:|---:|---:|"]
    for name,c in columns.items():
        s=c.get("numeric_summary", {})
        lines.append(f"| {name} | {c['inferred_numeric_type']} | {c['unique_count']} | {s.get('min', '')} | {s.get('max', '')} | {c['missing_marker_count']} |")
    lines += ["", "Types describe storage compatibility; integer codes may be categorical. Full frequencies follow below.", "", "## Review candidates (not invalidity findings)", ""]
    for candidate in reviews:
        if candidate["kind"] == "statistical_extremes":
            lines.append(f"- `{candidate['column']}`: {candidate['count']} records ({candidate['distinct_full_records']} distinct records) outside [{candidate['lower_fence']}, {candidate['upper_fence']}]; flagged value counts: {candidate['value_counts']}.")
        else:
            lines.append(f"- `{candidate['column']}={candidate['value']}`: {candidate['count']} records, {candidate['distinct_full_records']} distinct records; category meaning requires documentation.")
    lines += ["", "IQR flags use all repeated records and linear quantiles. Extremes are review candidates, not clinical judgments. All flagged source line numbers are in the JSON report.", "", "## Unresolved questions", ""]
    lines += [f"- {q}" for q in report["unresolved_questions"]]
    lines += ["", "## Interpretation", ""] + [f"- {s}" for s in report["interpretation"]]
    lines += ["", "## Counting and reproducibility", ""] + [f"- **{k}:** {v}" for k,v in report["methods"].items()]
    lines += ["", "Complete exact and feature-only groups appear separately in [duplicate_groups.md](duplicate_groups.md). All four raw/normalized group sets and flagged occurrences are in [audit_report.json](audit_report.json).", "", "## Source integrity and errors", "", f"- SHA-256 before: `{before_hash}`", f"- SHA-256 after: `{after_hash}`", f"- Source unchanged: **{unchanged}**", f"- Errors: {errors or 'None'}", "", "## Complete unique-value frequencies", ""]
    for name,c in columns.items():
        lines += [f"### {name}", "", "| Value | Count |", "|---|---:|"]
        lines += [f"| {json.dumps(v)} | {n} |" for v,n in c["value_frequencies"].items()]
        lines.append("")
    appendix = ["# Complete duplicate-group details", "", report["methods"]["counting"], "", report["methods"]["duplicates"], "", "Feature-only groups include groups that are also exact duplicates. They are not an additional disjoint set of duplicates.", ""]
    for title, result in [("Exact duplicates (all columns)", exact), ("Feature-only duplicates (target excluded)", features)]:
        appendix += [f"## {title}", ""]
        for g in result["groups"]:
            appendix += [f"### Group {g['group_id']} — {g['count']} occurrences", "", "Key: `"+json.dumps(g['key'],sort_keys=False)+"`", "", f"Target counts: {g['target_counts']}; conflicting labels: {g['conflicting_labels']}.", "", "| Logical record after header | Physical start line | Physical end line |", "|---:|---:|---:|"]
            appendix += [f"| {o['record_number']} | {o['line_start']} | {o['line_end']} |" for o in g["occurrences"]]
            appendix.append("")
    output.mkdir(parents=True, exist_ok=True)
    destinations[0].write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False)+"\n", encoding="utf-8")
    destinations[1].write_text("\n".join(lines)+"\n", encoding="utf-8")
    destinations[2].write_text("\n".join(appendix)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [str(p) for p in destinations], "source_unchanged": unchanged,
                      "rows": len(records), "columns": len(headers), "errors": errors}, indent=2))
    return 1 if errors else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        return run(args.input, args.output_dir)
    except (OSError, ValueError, UnicodeError, csv.Error, StopIteration) as exc:
        print(f"Audit failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
