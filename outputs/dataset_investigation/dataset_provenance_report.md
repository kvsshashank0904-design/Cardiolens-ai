# CardioLens AI: dataset provenance and data semantics investigation

Report completed: 2026-09-28. Public reference snapshots retrieved: 2026-09-27. Scope: read-only investigation of the supplied CSV and the completed experiments; no training, relabeling, data cleaning, or threshold changes.

## Main conclusion

**The local CSV is byte-for-byte identical to `heart.csv` in version 2 of Kaggle's `johnsmith88/heart-disease-dataset`.** Its 302 distinct records each match a different record in UCI's processed Cleveland data on eight unchanged fields. Deterministic recodings then reproduce all 14 local values for every matched record.

This establishes an exact public file/version match and strong, reproducible evidence of Cleveland-derived content. It does **not** establish who downloaded the project copy, the intermediary transformation history, why records were repeated, or why one UCI record is absent.

**Critical semantic conflict:** for all matched records, local `target=1` corresponds to UCI `num=0`, documented as absence; local `target=0` corresponds to UCI `num=1–4`, documented as presence. The Kaggle publisher description states the opposite local target direction. Its `thal` description also conflicts with the record correspondence. Do not use that description alone as the project's codebook. See [S1–S4] and the saved [record-level evidence](record_correspondence.json).

## 1. Existing project evidence

| Project evidence | What it establishes | What it does not establish |
|---|---|---|
| `MILF_Problem_Statements_Reference_Style (1).pdf`, p. 2, “Problem Statement 3: A Heart That Speaks in Data” | Educational classification objective, broad feature topics, requested evaluation measures, and a [Google Drive dataset folder](https://drive.google.com/drive/folders/1Op6s7UNVHqV8W2uFt8kxpW0G6svEdv64?usp=sharing). | No numeric label mapping, codebook, original collection history, or account of repetitions. The linked folder could not be read through the web tool; its contents were not verified. |
| `Lightweight ML Primer for Freshers.pdf`, pp. 9–12, 19, 28–29, 39 | Generic preprocessing/evaluation teaching; p. 39 describes the heart challenge; p. 19 characterizes examples as simplified teaching material. | Not a dataset-specific dictionary. Generic duplicate-removal examples do not explain these repetitions or authorize alteration. |
| `audit_report.json`, `group_manifest.csv`, `group_split.csv` | Local counts, exact values, duplicates, row references, feature-group assignments, and file identity. | No patient identities or original data-generation history. |
| `baseline_config.json`, `baseline_report.md`, both experiments' metrics and verification artifacts | Explicit modeling assumptions; group-safe evaluation; numeric positive class 1; source integrity. | Model performance cannot establish provenance or clinical label meaning. |

The PDFs are in `C:/Users/DELL/Desktop/DSAI SOCIETY/`. They are task-context documents, not authoritative measurement specifications. No missing fact has been filled in from their generic instructions.

## 2. Provenance: exact match versus historical inference

### Confirmed file identity

- Local source: `C:/Users/DELL/Desktop/DSAI SOCIETY/heart.csv`; 38,114 bytes.
- Local and downloaded version-2 CSV SHA-256: `ddb2996b2f4db2e00aad13f4518200179ff69f79093838e3c21ffa672ebec0f1`.
- Explicit version-2 download: [S4]. Archive contains `heart.csv`; the extracted bytes equal the local bytes, including order and formatting.
- Kaggle publisher API identifies dataset ID **216167**, reference **johnsmith88/heart-disease-dataset**, display owner **David Lapp**, version **2**, creation/update timestamp **2019-06-06T15:33:55.463Z**, with version note “Update data.” These are publisher metadata, not original collection dates. [S3]

**Confidence: confirmed content/version match.** The project copy could have arrived through Kaggle, Drive, or another identical mirror. There is no acquisition receipt connecting the local file to a particular download event.

### Upstream record correspondence

UCI's historical documentation identifies four collection locations and a 303-record Cleveland subset; the repository describes 13 features and an outcome field `num`. [S1, S2] This does not mean the local 1,025-row file contains four independent cohorts.

Comparison method:

1. Read local records without altering them; group exact copies only in memory for comparison.
2. Match on `age`, `sex`, `trestbps`, `chol`, `fbs`, `thalach`, `exang`, and `oldpeak` using exact decimal equality. Neither target nor any recoded field participates in finding matches.
3. Each of the **302** local distinct records has **exactly one** candidate among the **303** UCI processed Cleveland records. No local record is unmatched or ambiguous.
4. Infer the remaining code correspondences from those matches, then verify all 14 values after recoding. All **302** records pass; every one of the 1,025 local rows belongs to one of them.

**Confidence: confirmed correspondence for the downloaded snapshots; high-confidence Cleveland derivation.** The comparison is empirical reconstruction, not an authenticated transformation log. Matching records does not independently authenticate original measurement quality or patient identity.

One UCI record is absent: **physical line 185**, with `age=60`, `sex=0`, `cp=4`, `trestbps=158`, `chol=305`, `fbs=0`, `restecg=2`, `thalach=161`, `exang=0`, `oldpeak=0`, `slope=1`, `ca=0`, `thal=3`, `num=1`. Why it is absent is unknown. This is a finding about the supplied processed Cleveland snapshot, not a claim about all historical versions. [S5; record-level evidence]

### Publisher documentation conflicts

- **Target:** publisher metadata assigns local 1 to presence. Empirical correspondence instead maps **164 distinct local label-1 records to UCI num=0**; all **138 local label-0 records map to UCI num>0**. Across repeated rows these are 526 and 499 rows, respectively.
- **Thal:** publisher metadata assigns its listed codes differently from the file-to-UCI correspondence and does not account for local code 3. The actual observed correspondence is in the table below.
- **Missingness:** a CSV with no blanks can still encode upstream missingness. Local `ca=4` and `thal=0` correspond exactly to upstream `?` entries. UCI's general historical notes also mention `-9.0`; the specific processed Cleveland file inspected here uses `?`. These conventions must not be conflated. [S2–S5]

The publisher's codebook is therefore not reliable enough to override the row evidence. The intended downstream label convention and the transformation author's intent still require clarification.

## 3. All 14 columns: evidence-based working dictionary

Confidence is about applicability to this exact file, not clinical validity. **High** means a UCI definition plus complete record correspondence; **high correspondence / disputed intent** means numerical mapping is verified but publisher prose conflicts; **partial** means a definition is available but a unit is not explicitly documented. Local categorical codes below are derived from the matched records, not copied blindly from UCI codes.

| Column | Definition supported by UCI | Local units or categories | Evidence | Confidence |
|---|---|---|---|---|
| `age` | Age | Years; observed 29–77 | S1/S2; unchanged anchor | High |
| `sex` | Recorded sex code | 0 female; 1 male | S2; unchanged anchor | High; historical coding only |
| `cp` | Chest-pain category | 0 asymptomatic; 1 atypical angina; 2 non-anginal pain; 3 typical angina | S2 plus empirical UCI→local mapping: 4→0, 2→1, 3→2, 1→3 | High |
| `trestbps` | Resting pressure on admission | mm Hg; observed 94–200 | S1/S2; unchanged anchor | High |
| `chol` | Serum cholesterol | mg/dL; observed 126–564 | S1/S2; unchanged anchor | High |
| `fbs` | Indicator for fasting blood sugar above 120 mg/dL | 0 false; 1 true; this is an indicator, not a glucose measurement | S1/S2; unchanged anchor | High |
| `restecg` | Resting ECG category | 0 probable/definite left-ventricular hypertrophy; 1 normal; 2 ST–T abnormality | S2; UCI→local: 2→0, 0→1, 1→2 | High |
| `thalach` | Maximum achieved heart rate | Observed 71–202; the cited UCI definition does not explicitly state a unit. Do not mark bpm as verified from this source. | S1/S2; unchanged anchor | High definition; partial units |
| `exang` | Exercise-induced angina indicator | 0 no; 1 yes | S2; unchanged anchor | High |
| `oldpeak` | Exercise-related ST depression relative to rest | Observed 0–6.2; unit not explicitly stated in the cited definition. Do not silently assign mm or mV. | S1/S2; unchanged anchor | High definition; partial units |
| `slope` | Peak-exercise ST-segment slope | 0 downsloping; 1 flat; 2 upsloping | S2; UCI→local: 3→0, 2→1, 1→2 | High |
| `ca` | Fluoroscopy-colored major-vessel count | 0–3 retain their counts; **4 corresponds to upstream missing `?`**, not a documented count of four | S2/S5; 4 matched distinct records, 18 local rows | High correspondence; missing-code intent undocumented |
| `thal` | UCI defect-status variable named `thal` | **0 corresponds to missing `?`**; 1 fixed defect; 2 normal; 3 reversible defect. Do not expand the name to an unsupported disease diagnosis. | S2/S5; UCI→local: ?→0, 6→1, 3→2, 7→3; missing corresponds to 2 distinct records/7 rows | High correspondence; publisher mapping conflicts |
| `target` | Recoding of UCI `num` outcome | **1 matches num=0 (documented absence); 0 matches num=1–4 (documented presence).** No severity information remains in local 0. | S1/S2/S5 plus all 302 matched records; contradicts S3 description | High correspondence / disputed publisher intent |

The table is a **documented working interpretation**, not authorization to relabel, impute, or reinterpret existing artifacts silently. UCI's definitions are authoritative for its reference data; applying them here relies on the explicitly recorded correspondence. The usual 0-based assumption is unsafe: several local codes are reordered rather than simply reduced by one.

## 4. Repeated-record investigation

### Confirmed from the CSV alone

- 1,025 rows, 14 columns, 302 distinct feature combinations and feature/label records.
- 723 additional copies beyond one per distinct record, or **70.54%** of rows.
- **187 groups occur 3 times, 114 occur 4 times, and 1 occurs 8 times:** `187×3 + 114×4 + 1×8 = 1,025`.
- Every group has a consistent label. There is no label-conflict explanation for the repetitions.
- The eight-copy group has `age=38`, `sex=1`, `cp=2`, `trestbps=138`, `chol=175`, `fbs=0`, `restecg=1`, `thalach=173`, `exang=0`, `oldpeak=0`, `slope=2`, `ca=4`, `thal=2`, `target=1`.

### What the external comparison adds

All repeated local records are copies of one of the 302 corresponding Cleveland-derived patterns. The binary class counts after counting patterns once are 138 zeros / 164 ones. The upstream subset has all 164 `num=0` records and 138 of 139 `num>0` records. These facts strengthen the evidence for a repeated, recoded derivative rather than 1,025 newly documented observations.

### What remains unknown

The pattern is compatible with deliberate expansion, resampling, or repeated concatenation, but does not identify which occurred, its seed, its purpose, or the role of the eight-copy record. It does not prove erroneous records, independent repeat visits, or distinct patients. No collection timestamp or patient identifier resolves those alternatives. The absent upstream record cannot be attributed to a specific cleaning rule without a transformation history.

Repeated rows alter training weights, preprocessing statistics, and row-weighted metrics. They do not add new feature/label combinations or justify treating 1,025 rows as independent evidence. The completed group-safe experiments prevent identical feature groups from crossing partitions; they do not establish patient-level separation or resolve upstream dependence.

## 5. Implications for existing experiments

The saved calculations remain calculations for **numeric target 1** and have not been modified. Their “sensitivity” must not be presented as sensitivity for disease presence: the matched upstream interpretation points in the opposite direction. Similarly, probability of numeric label 1 must not be labeled disease risk.

The pipelines retained all categorical codes and did not impute. The investigation now shows that `ca=4` and `thal=0` correspond to reference missingness; previous statements of no blank/text-marker cells remain true, but “no missing information” would be false. A future explicitly versioned experiment could address this only after review; none was run here.

These semantic issues cannot be resolved by good model scores. The primary and repetition-weighted artifacts remain historical, reproducible numeric-label experiments, with this report as a separate evidence supplement.

## 6. Unresolved questions, risks, and resolving evidence

| Question | Risk | Evidence needed to resolve it |
|---|---|---|
| How did the project obtain this exact file? | Incorrect chain-of-custody attribution | Organizer's original download URL/version, dated receipt, Drive revision metadata, and matching checksum |
| Which transformation created the recodings and target reversal? | Opposite interpretation of predictions and errors | Original transformation script/version or publisher correction explicitly tied to version-2 bytes |
| Why are records repeated 3/4/8 times, and why is UCI line 185 absent? | Unsupported sample-size or cleaning claims | Reproducible expansion/filtering code, original input files, seed, and rationale |
| What was the intended treatment of `ca=4` and `thal=0`? | Missingness mistaken for measurement categories | Transformation code and a version-specific codebook; row correspondence already verifies their upstream missing entries |
| What units were intended for `thalach` and `oldpeak`? | Incorrect input descriptions or ranges | Original measurement protocol or authoritative version-specific dictionary explicitly specifying units |
| What are the original sampling dates, eligibility criteria, and measurement timing for these records? | Unsupported population or prediction-time assumptions; possible unavailable-at-use-time features | Study protocol, original collection documentation, and an explicit intended prediction setting |
| Do multiple feature records belong to the same patient? | Unverified independence despite group-safe evaluation | Valid de-identified patient/visit keys or trusted linkage metadata; feature equality alone is insufficient |
| What redistribution terms apply to the exact derivative? | Unclear attribution/redistribution status | Publisher's explicit derivative license and attribution history. UCI currently lists CC BY 4.0; Kaggle metadata says Unknown. Neither is silently substituted for the other's metadata. [S1, S3] |

## 7. Suitability decision and recommended next step

**Conditionally suitable for a transparent educational data-audit and ML-methods prototype; not yet sufficiently documented for a heart-disease risk-screening interface.** The file/version match and reconstructed mappings substantially improve documentation, but contradictory publisher prose, unknown repetition history, incomplete units, and absent patient linkage remain material.

Keep the prototype framed as classification of numeric labels and an illustration of provenance, missing codes, and duplicate-safe evaluation. Before presenting disease-labeled predictions or human-readable measurement inputs, obtain a reconciled version-specific codebook and record the evidence-based label direction explicitly. Ask the provider for the transformation history and missing-code policy. Do not silently retrofit either completed experiment.

No claim of clinical validity, diagnostic accuracy, patient-level independence, or generalization to new patients follows from this investigation.

## 8. Reproduction, integrity, and limitations of access

- [verify_provenance.py](verify_provenance.py) reproduces the exact-byte comparison, record linkage, inferred mappings, and integrity checks from saved public reference snapshots. Run `python -B outputs/dataset_investigation/verify_provenance.py` from the workspace root.
- [record_correspondence.json](record_correspondence.json) contains all 302 matched group IDs, source record/physical-line references, UCI line numbers, code-pair counts, and the unmatched UCI record.
- [sources/source_manifest.json](sources/source_manifest.json) records exact URLs, byte sizes, retrieval date, and SHA-256 hashes for the snapshots. No transient signed download URL is required for reproduction.
- [investigation_verification.json](investigation_verification.json): **PASS**; **39 pre-existing protected artifacts** plus the original CSV retain their initial hashes. Zero models trained; neither experiment was edited.
- Initial restricted-network retrieval failed; the authorized network retry succeeded for UCI and Kaggle. The Drive reference remains uninspected. This access limitation does not weaken the independently verified Kaggle byte match, but leaves the project transfer route unknown.

## Sources

**S1 — UCI repository record**, “Heart Disease,” Dataset Information, Variables Table, Additional Variable Information, and citation/license metadata: https://archive.ics.uci.edu/dataset/45/heart+disease . Dataset DOI: https://doi.org/10.24432/C52P4X . This describes the UCI collection, not the local derivative's processing history.

**S2 — UCI original documentation**, `heart-disease.names`, sections 2 (Source Information), 4 (Relevant Information), 5 (Number of Instances), 7 (Attribute Information), 9 (Missing Attribute Values), 10 (Class Distribution): https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/heart-disease.names . Saved as `sources/uci_names.txt`.

**S3 — Kaggle publisher metadata**, dataset page https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset and API https://www.kaggle.com/api/v1/datasets/view/johnsmith88/heart-disease-dataset . API fields `description`, `currentVersionNumber`, `versions`, and `licenseName` were inspected. Saved as `sources/kaggle_view.json`. Publisher prose is explicitly contradicted by record-level evidence on target/thal coding; it is not accepted uncritically.

**S4 — Explicit Kaggle version-2 archive:** https://www.kaggle.com/api/v1/datasets/download/johnsmith88/heart-disease-dataset?datasetVersionNumber=2 . Saved as `sources/kaggle_version2.zip`; archive SHA-256 `44c9dee9d3072915a677a2d1f15ad6269ca0a1a9258ca9b100789f2e377e4974`.

**S5 — UCI processed Cleveland numeric records:** https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data . Saved as `sources/uci_cleveland.data`; SHA-256 `a74b7efa387bc9d108d7d0115d831fe9b414b29ae7124f331b622b4efa0427c8`. This is the direct comparison source; no third-party notebook was used as authority for recoding.
