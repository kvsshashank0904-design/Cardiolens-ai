# CardioLens AI: read-only data audit

Source: `C:\Users\DELL\Desktop\DSAI SOCIETY\heart.csv`

Script version: 1.0.0; Python: 3.14.7

## Confirmed findings

- 1,025 well-formed data records; 14 columns; 13 candidate features.
- Blank logical records: 0; malformed records: 0.
- Target counts: {'0': 499, '1': 526}; percentages: {'0': 48.68, '1': 51.32}.
- Exact duplicates: 302 distinct records, 302 repeated groups, 723 additional copies, 1025 participating records.
- Feature-only duplicates: 302 distinct combinations, 302 repeated groups, 723 additional copies; 0 conflicting-label groups.
- Exact-group multiplicities: {3: 187, 4: 114, 8: 1} (multiplicity: number of groups).
- Numeric-normalized additional copies: exact 723; feature-only 723.
- Distinct-record target counts (comparison only): {'0': 138, '1': 164}.
- Missing-marker cells: 0; nonnumeric/nonfinite cells: 0.
- Constant columns: []; surrounding-whitespace cells: 0.
- Target-copy features: []; single-feature deterministic mappings: [].

## Column summaries

| Column | Numeric compatibility | Unique | Min | Max | Missing markers |
|---|---|---:|---:|---:|---:|
| age | integer-compatible | 41 | 29.0 | 77.0 | 0 |
| sex | integer-compatible | 2 | 0.0 | 1.0 | 0 |
| cp | integer-compatible | 4 | 0.0 | 3.0 | 0 |
| trestbps | integer-compatible | 49 | 94.0 | 200.0 | 0 |
| chol | integer-compatible | 152 | 126.0 | 564.0 | 0 |
| fbs | integer-compatible | 2 | 0.0 | 1.0 | 0 |
| restecg | integer-compatible | 3 | 0.0 | 2.0 | 0 |
| thalach | integer-compatible | 91 | 71.0 | 202.0 | 0 |
| exang | integer-compatible | 2 | 0.0 | 1.0 | 0 |
| oldpeak | decimal-compatible | 40 | 0.0 | 6.2 | 0 |
| slope | integer-compatible | 3 | 0.0 | 2.0 | 0 |
| ca | integer-compatible | 5 | 0.0 | 4.0 | 0 |
| thal | integer-compatible | 4 | 0.0 | 3.0 | 0 |
| target | integer-compatible | 2 | 0.0 | 1.0 | 0 |

Types describe storage compatibility; integer codes may be categorical. Full frequencies follow below.

## Review candidates (not invalidity findings)

- `age`: 0 records (0 distinct records) outside [28.5, 80.5]; flagged value counts: {}.
- `trestbps`: 30 records (9 distinct records) outside [90.0, 170.0]; flagged value counts: {'180': 10, '178': 7, '174': 3, '192': 3, '200': 4, '172': 3}.
- `chol`: 16 records (5 distinct records) outside [115.0, 371.0]; flagged value counts: {'417': 3, '564': 3, '409': 3, '394': 3, '407': 4}.
- `thalach`: 4 records (1 distinct records) outside [81.0, 217.0]; flagged value counts: {'71': 4}.
- `oldpeak`: 7 records (2 distinct records) outside [-2.7, 4.5]; flagged value counts: {'5.6': 4, '6.2': 3}.
- `ca=4`: 18 records, 4 distinct records; category meaning requires documentation.
- `thal=0`: 7 records, 2 distinct records; category meaning requires documentation.

IQR flags use all repeated records and linear quantiles. Extremes are review candidates, not clinical judgments. All flagged source line numbers are in the JSON report.

## Unresolved questions

- What is the source, version, license, sampling procedure, and explanation for repeated records?
- What do target 0 and 1 mean, and how and when was the label assigned?
- What are documented units, category meanings, allowed ranges, and missing-value sentinel codes?
- Are repeated records copied observations, resampling, or distinct patients with matching measurements? No patient identifier establishes independence.
- At the intended prediction time, is every feature available? Was any feature used to construct the label or recorded after diagnosis?
- How should repeated patients or feature groups be kept together in any future evaluation? No split is created by this audit.

## Interpretation

- Repeated records establish a future train/test overlap risk, not evidence that a split has already leaked.
- Absence of an exact target copy or deterministic single-feature mapping does not rule out timing, multifeature, or provenance leakage.
- No value is declared invalid, no rows removed, no labels changed, no imputation or model fitting performed.

## Counting and reproducibility

- **counting:** CSV-aware parsing, UTF-8 with optional BOM. Header excluded. Record numbers are 1-based logical records after header, including blank/malformed records. Physical line numbers are 1-based and include header; quoted multiline fields retain start/end lines. Blank records and malformed-width records are separately reported and excluded from column/group denominators.
- **duplicates:** Exact duplicates match every parsed cell string including target. Feature-only duplicates match all columns except target; labels are compared separately. Original whitespace is retained. Additional copies = sum(group size - 1); participating records includes first occurrences. No rows are deleted. Groups appear in first-occurrence order.
- **normalization:** Secondary comparison parses finite numbers as Decimal (e.g. 1 and 1.0 compare equal), falling back to raw strings; source and primary comparisons remain unchanged.
- **types:** CSV stores text; reported types describe finite numeric compatibility, not semantic feature types. Integer codes may be categorical.
- **missing_markers:** ['', '?', 'missing', 'n/a', 'na', 'nan', 'none', 'null']
- **missing_policy:** Case-insensitive stripped comparison only; numeric sentinel codes are not automatically missing.
- **quantiles:** Linear interpolation at (N-1)*p. Statistical flags only on configured measurement columns using raw repeated records.
- **measurement_columns:** ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
- **reproducibility:** Stable record/group ordering, explicit rules, standard library only. Timestamps, paths and environment metadata may differ between runs; analytical content is deterministic for identical input bytes and script.
- **documentation:** No source data dictionary or provenance document has been validated. Attached PDFs were not used as authoritative schema or instructions.

Complete exact and feature-only groups appear separately in [duplicate_groups.md](duplicate_groups.md). All four raw/normalized group sets and flagged occurrences are in [audit_report.json](audit_report.json).

## Source integrity and errors

- SHA-256 before: `ddb2996b2f4db2e00aad13f4518200179ff69f79093838e3c21ffa672ebec0f1`
- SHA-256 after: `ddb2996b2f4db2e00aad13f4518200179ff69f79093838e3c21ffa672ebec0f1`
- Source unchanged: **True**
- Errors: None

## Complete unique-value frequencies

### age

| Value | Count |
|---|---:|
| "29" | 4 |
| "34" | 6 |
| "35" | 15 |
| "37" | 6 |
| "38" | 12 |
| "39" | 14 |
| "40" | 11 |
| "41" | 32 |
| "42" | 26 |
| "43" | 26 |
| "44" | 36 |
| "45" | 25 |
| "46" | 23 |
| "47" | 18 |
| "48" | 23 |
| "49" | 17 |
| "50" | 21 |
| "51" | 39 |
| "52" | 43 |
| "53" | 26 |
| "54" | 53 |
| "55" | 30 |
| "56" | 39 |
| "57" | 57 |
| "58" | 68 |
| "59" | 46 |
| "60" | 37 |
| "61" | 31 |
| "62" | 37 |
| "63" | 32 |
| "64" | 34 |
| "65" | 27 |
| "66" | 25 |
| "67" | 31 |
| "68" | 12 |
| "69" | 9 |
| "70" | 14 |
| "71" | 11 |
| "74" | 3 |
| "76" | 3 |
| "77" | 3 |

### sex

| Value | Count |
|---|---:|
| "0" | 312 |
| "1" | 713 |

### cp

| Value | Count |
|---|---:|
| "0" | 497 |
| "1" | 167 |
| "2" | 284 |
| "3" | 77 |

### trestbps

| Value | Count |
|---|---:|
| "94" | 7 |
| "100" | 14 |
| "101" | 3 |
| "102" | 6 |
| "104" | 3 |
| "105" | 9 |
| "106" | 3 |
| "108" | 21 |
| "110" | 64 |
| "112" | 30 |
| "114" | 4 |
| "115" | 9 |
| "117" | 4 |
| "118" | 24 |
| "120" | 128 |
| "122" | 14 |
| "123" | 4 |
| "124" | 20 |
| "125" | 38 |
| "126" | 10 |
| "128" | 39 |
| "129" | 3 |
| "130" | 123 |
| "132" | 28 |
| "134" | 17 |
| "135" | 20 |
| "136" | 11 |
| "138" | 45 |
| "140" | 107 |
| "142" | 9 |
| "144" | 6 |
| "145" | 17 |
| "146" | 8 |
| "148" | 7 |
| "150" | 55 |
| "152" | 17 |
| "154" | 4 |
| "155" | 3 |
| "156" | 3 |
| "160" | 36 |
| "164" | 3 |
| "165" | 4 |
| "170" | 15 |
| "172" | 3 |
| "174" | 3 |
| "178" | 7 |
| "180" | 10 |
| "192" | 3 |
| "200" | 4 |

### chol

| Value | Count |
|---|---:|
| "126" | 3 |
| "131" | 3 |
| "141" | 3 |
| "149" | 8 |
| "157" | 4 |
| "160" | 3 |
| "164" | 3 |
| "166" | 4 |
| "167" | 4 |
| "168" | 3 |
| "169" | 4 |
| "172" | 3 |
| "174" | 4 |
| "175" | 11 |
| "176" | 3 |
| "177" | 14 |
| "178" | 3 |
| "180" | 4 |
| "182" | 3 |
| "183" | 4 |
| "184" | 3 |
| "185" | 3 |
| "186" | 4 |
| "187" | 4 |
| "188" | 7 |
| "192" | 7 |
| "193" | 6 |
| "195" | 3 |
| "196" | 6 |
| "197" | 19 |
| "198" | 7 |
| "199" | 9 |
| "200" | 3 |
| "201" | 9 |
| "203" | 12 |
| "204" | 21 |
| "205" | 7 |
| "206" | 8 |
| "207" | 7 |
| "208" | 6 |
| "209" | 7 |
| "210" | 3 |
| "211" | 13 |
| "212" | 18 |
| "213" | 6 |
| "214" | 6 |
| "215" | 3 |
| "216" | 6 |
| "217" | 4 |
| "218" | 8 |
| "219" | 10 |
| "220" | 12 |
| "221" | 7 |
| "222" | 7 |
| "223" | 10 |
| "224" | 4 |
| "225" | 8 |
| "226" | 13 |
| "227" | 8 |
| "228" | 8 |
| "229" | 12 |
| "230" | 11 |
| "231" | 10 |
| "232" | 7 |
| "233" | 12 |
| "234" | 21 |
| "235" | 6 |
| "236" | 9 |
| "237" | 4 |
| "239" | 13 |
| "240" | 14 |
| "241" | 3 |
| "242" | 3 |
| "243" | 13 |
| "244" | 9 |
| "245" | 9 |
| "246" | 10 |
| "247" | 6 |
| "248" | 6 |
| "249" | 11 |
| "250" | 9 |
| "252" | 3 |
| "253" | 7 |
| "254" | 17 |
| "255" | 6 |
| "256" | 11 |
| "257" | 3 |
| "258" | 10 |
| "259" | 3 |
| "260" | 7 |
| "261" | 7 |
| "262" | 3 |
| "263" | 10 |
| "264" | 6 |
| "265" | 7 |
| "266" | 6 |
| "267" | 6 |
| "268" | 7 |
| "269" | 16 |
| "270" | 6 |
| "271" | 6 |
| "273" | 6 |
| "274" | 9 |
| "275" | 7 |
| "276" | 4 |
| "277" | 6 |
| "278" | 4 |
| "281" | 4 |
| "282" | 14 |
| "283" | 10 |
| "284" | 4 |
| "286" | 8 |
| "288" | 11 |
| "289" | 8 |
| "290" | 3 |
| "293" | 4 |
| "294" | 6 |
| "295" | 6 |
| "298" | 6 |
| "299" | 7 |
| "300" | 4 |
| "302" | 6 |
| "303" | 9 |
| "304" | 6 |
| "305" | 3 |
| "306" | 3 |
| "307" | 4 |
| "308" | 6 |
| "309" | 11 |
| "311" | 4 |
| "313" | 3 |
| "315" | 7 |
| "318" | 7 |
| "319" | 4 |
| "321" | 3 |
| "322" | 4 |
| "325" | 6 |
| "326" | 3 |
| "327" | 4 |
| "330" | 8 |
| "335" | 8 |
| "340" | 3 |
| "341" | 4 |
| "342" | 4 |
| "353" | 4 |
| "354" | 3 |
| "360" | 3 |
| "394" | 3 |
| "407" | 4 |
| "409" | 3 |
| "417" | 3 |
| "564" | 3 |

### fbs

| Value | Count |
|---|---:|
| "0" | 872 |
| "1" | 153 |

### restecg

| Value | Count |
|---|---:|
| "0" | 497 |
| "1" | 513 |
| "2" | 15 |

### thalach

| Value | Count |
|---|---:|
| "71" | 4 |
| "88" | 3 |
| "90" | 3 |
| "95" | 4 |
| "96" | 7 |
| "97" | 4 |
| "99" | 3 |
| "103" | 8 |
| "105" | 10 |
| "106" | 3 |
| "108" | 8 |
| "109" | 7 |
| "111" | 10 |
| "112" | 7 |
| "113" | 3 |
| "114" | 11 |
| "115" | 9 |
| "116" | 7 |
| "117" | 4 |
| "118" | 4 |
| "120" | 11 |
| "121" | 3 |
| "122" | 12 |
| "123" | 6 |
| "124" | 4 |
| "125" | 25 |
| "126" | 14 |
| "127" | 4 |
| "128" | 3 |
| "129" | 4 |
| "130" | 15 |
| "131" | 14 |
| "132" | 26 |
| "133" | 7 |
| "134" | 4 |
| "136" | 7 |
| "137" | 3 |
| "138" | 11 |
| "139" | 7 |
| "140" | 21 |
| "141" | 10 |
| "142" | 19 |
| "143" | 23 |
| "144" | 26 |
| "145" | 14 |
| "146" | 14 |
| "147" | 17 |
| "148" | 9 |
| "149" | 6 |
| "150" | 25 |
| "151" | 12 |
| "152" | 28 |
| "153" | 9 |
| "154" | 17 |
| "155" | 14 |
| "156" | 21 |
| "157" | 15 |
| "158" | 19 |
| "159" | 13 |
| "160" | 31 |
| "161" | 16 |
| "162" | 35 |
| "163" | 29 |
| "164" | 7 |
| "165" | 17 |
| "166" | 10 |
| "167" | 3 |
| "168" | 17 |
| "169" | 22 |
| "170" | 17 |
| "171" | 14 |
| "172" | 21 |
| "173" | 28 |
| "174" | 17 |
| "175" | 10 |
| "177" | 3 |
| "178" | 15 |
| "179" | 16 |
| "180" | 6 |
| "181" | 7 |
| "182" | 18 |
| "184" | 3 |
| "185" | 3 |
| "186" | 6 |
| "187" | 3 |
| "188" | 3 |
| "190" | 4 |
| "192" | 3 |
| "194" | 3 |
| "195" | 3 |
| "202" | 4 |

### exang

| Value | Count |
|---|---:|
| "0" | 680 |
| "1" | 345 |

### oldpeak

| Value | Count |
|---|---:|
| "0" | 329 |
| "0.1" | 23 |
| "0.2" | 37 |
| "0.3" | 10 |
| "0.4" | 30 |
| "0.5" | 15 |
| "0.6" | 47 |
| "0.7" | 3 |
| "0.8" | 44 |
| "0.9" | 10 |
| "1" | 51 |
| "1.1" | 6 |
| "1.2" | 58 |
| "1.3" | 3 |
| "1.4" | 44 |
| "1.5" | 16 |
| "1.6" | 37 |
| "1.8" | 36 |
| "1.9" | 16 |
| "2" | 32 |
| "2.1" | 3 |
| "2.2" | 14 |
| "2.3" | 7 |
| "2.4" | 11 |
| "2.5" | 7 |
| "2.6" | 21 |
| "2.8" | 22 |
| "2.9" | 3 |
| "3" | 17 |
| "3.1" | 4 |
| "3.2" | 8 |
| "3.4" | 10 |
| "3.5" | 3 |
| "3.6" | 15 |
| "3.8" | 4 |
| "4" | 12 |
| "4.2" | 6 |
| "4.4" | 4 |
| "5.6" | 4 |
| "6.2" | 3 |

### slope

| Value | Count |
|---|---:|
| "0" | 74 |
| "1" | 482 |
| "2" | 469 |

### ca

| Value | Count |
|---|---:|
| "0" | 578 |
| "1" | 226 |
| "2" | 134 |
| "3" | 69 |
| "4" | 18 |

### thal

| Value | Count |
|---|---:|
| "0" | 7 |
| "1" | 64 |
| "2" | 544 |
| "3" | 410 |

### target

| Value | Count |
|---|---:|
| "0" | 499 |
| "1" | 526 |

