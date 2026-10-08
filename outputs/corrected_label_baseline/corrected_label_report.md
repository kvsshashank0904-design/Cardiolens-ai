# Experiment 3: corrected-label baseline

## Design and evidence

The label transformation is **disease_present = 1 - original_target = int(matched UCI num > 0)**. All 302 saved feature groups were independently matched to unique UCI records using the eight unchanged anchor fields, then checked against the saved record-level evidence. Every source row retains its original label alongside the new label. No ambiguous matches were found.

Local ca=4 and thal=0 were verified in both directions against UCI missing entries. Only in the derived data, these codes become blanks/NaN. The derived file retains original_ca, original_thal, original_target, missingness flags, source record/physical line numbers, UCI num/line, and saved group/partition/fold IDs. All 1,025 original rows remain represented. No patient identifier is inferred.

Evidence: ../dataset_investigation/record_correspondence.json; ../dataset_investigation/dataset_provenance_report.md; the pinned UCI snapshot and codebook under ../dataset_investigation/sources/. Public sources: [UCI documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/heart-disease.names) and [processed Cleveland records](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data). The record correspondence overrides contradictory publisher prose for this derived experiment; it does not establish the historical transformation author's intent.

## Fixed design and necessary changes

- Fixed: existing feature group IDs, seed 42, saved development/test assignments and five folds; one first-occurrence row per training group; logistic regression L2/C=1/lbfgs/max_iter=2000/tol=0.0001/no class weights; numeric scaling, nominal one-hot feature roles, unknown-category handling, and threshold 0.5.
- Changed: positive-label direction; ca/thal sentinel decoding; categorical missing-value preprocessing. Logistic regression is fixed rather than reselecting between models. The earlier majority model is not rerun. No hyperparameter or threshold search.
- Primary option explicit_missing: replace NaN by -1 inside the categorical pipeline and one-hot encode it as explicitly missing. It is never described as a valid vessel count or defect state. This retains missingness without guessing its hidden value.
- Sensitivity option mode_plus_indicator: learn the modal category from training groups only, fill NaN with it, and append two fixed ca/thal missingness indicators. Modes are assumptions, not recovered measurements. Missing indicators exist even if a training fold has no missing entry.
- All learned transformations fit only within each fold's training data. Constant decoding uses documented codes, not fitted statistics. New model inputs must decode the two sentinels to NaN before using the saved pipelines.
- Both options were specified before fitting. Both are reported without choosing a winner from final test results. The missingness mechanism remains unknown; comparing these options is not proof that either is correct.

The original grouping remains fixed even if transformed inputs coincide. This preserves the same feature-pattern separation as the earlier experiments, not patient-level independence.

## Counts and results

| Partition | Groups | Original rows | Corrected group labels 0 / 1 | Corrected row labels 0 / 1 |
|---|---:|---:|---|---|
| all | 302 | 1025 | 164 / 138 | 526 / 499 |
| development | 241 | 811 | 131 / 110 | 416 / 395 |
| test | 61 | 214 | 33 / 28 | 110 / 104 |

Final fitting uses 241 representative rows; test evaluation uses 61 groups or their 214 original rows. No repeated-row training is added in Experiment 3. Fold counts and both metric views are in corrected_label_metrics.json.

| Option | CV view | Mean AUC | Fold sample SD |
|---|---|---:|---:|
| explicit_missing | distinct_group | 0.944755 | 0.026444 |
| explicit_missing | original_row_weighted | 0.945624 | 0.028318 |
| mode_plus_indicator | distinct_group | 0.945105 | 0.025741 |
| mode_plus_indicator | original_row_weighted | 0.946099 | 0.027417 |

| Option | Test view | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| explicit_missing | distinct_group | 0.642857 | 0.878788 | 0.818182 | 0.720000 | 0.770492 | 0.840909 |
| explicit_missing | original_row_weighted | 0.634615 | 0.872727 | 0.825000 | 0.717391 | 0.757009 | 0.838112 |
| mode_plus_indicator | distinct_group | 0.642857 | 0.909091 | 0.857143 | 0.734694 | 0.786885 | 0.843074 |
| mode_plus_indicator | original_row_weighted | 0.634615 | 0.909091 | 0.868421 | 0.733333 | 0.775701 | 0.843007 |

**explicit_missing, distinct_group:** confusion matrix `[[29, 4], [10, 18]]`; denominators `{'sensitivity': 28, 'specificity': 33, 'precision': 22, 'f1': 50, 'accuracy': 61, 'roc_auc_positive_negative_pairs': 924}`.

**explicit_missing, original_row_weighted:** confusion matrix `[[96, 14], [38, 66]]`; denominators `{'sensitivity': 104, 'specificity': 110, 'precision': 80, 'f1': 184, 'accuracy': 214, 'roc_auc_positive_negative_pairs': 11440}`.

**mode_plus_indicator, distinct_group:** confusion matrix `[[30, 3], [10, 18]]`; denominators `{'sensitivity': 28, 'specificity': 33, 'precision': 21, 'f1': 49, 'accuracy': 61, 'roc_auc_positive_negative_pairs': 924}`.

**mode_plus_indicator, original_row_weighted:** confusion matrix `[[100, 10], [38, 66]]`; denominators `{'sensitivity': 104, 'specificity': 110, 'precision': 76, 'f1': 180, 'accuracy': 214, 'roc_auc_positive_negative_pairs': 11440}`.

Matrices are [[TN, FP], [FN, TP]] with rows=true 0/1, columns=predicted 0/1. Sensitivity now refers to the matched UCI presence class; specificity to the absence class. ROC-AUC uses probability_disease_present. Undefined metrics are null. CV mean/SD describe five folds and are not confidence intervals. Row-weighted metrics expand the same group predictions, without another prediction call.

## What these results mean

Observed result: explicit_missing has test-group AUC 0.840909, sensitivity 18/28 = 0.642857, and specificity 29/33 = 0.878788. Mode-plus-indicator has AUC 0.843074, the same sensitivity, and specificity 30/33 = 0.909091. Both miss 10 corrected-positive groups. The latter has one fewer false-positive group; this descriptive difference does not establish superiority or statistical significance. The primary option remains the one designated before fitting.

For explicit_missing, AUC and accuracy match Experiment 1, while the corrected sensitivity equals its old numeric-label specificity. The missing-code one-hot representation is equivalent up to category-column order; recognizing missingness and reversing the target should not be presented as evidence of improved prediction.

Earlier sensitivities concerned the opposite numeric class and cannot be compared directly as disease-presence sensitivities. Reversing binary labels and probability direction alone need not change discrimination or accuracy; changes in those measures can also reflect the missing-data treatment. No improvement claim is made from corrected terminology.

The holdout has been inspected in earlier experiments and in provenance analysis. This is a secondary exploratory, shared-holdout comparison, not independent test performance. Upstream label values were consulted for semantic validation, not model/threshold selection. No test rows enter fitting or learned preprocessing.

Unknowns remain: acquisition route, transformation/repetition history, missingness mechanism, one absent UCI record, some units, and patient linkage. The derived positive class follows documented UCI outcome coding; it is not a newly validated clinical diagnosis. These results establish no clinical validity, patient-level generalization, or performance on new patients. Repetition is not independent evidence. No UI was built.

## Verification and reproduction

Execution and independent verification both finished with **PASS** and empty error lists. All 12 fits completed without convergence errors. The original CSV and **49 pre-existing output files**, including the earlier 39 protected artifacts and the provenance investigation, retained their frozen hashes. All 302 label mappings and 1,025 derived rows were verified; no ambiguous matches were found. The verifier made no new model fits or prediction calls.

Run the separate verifier after this script. corrected_label_verification.json records PASS/FAIL and explicit errors; it reconstructs mappings and metrics independently. Config contains frozen hashes for every pre-existing output, including both experiments and provenance files. Source checksum is checked before and after.

Use Python 3.12 with the unchanged ../baseline_requirements.txt pins. From the workspace root:

```powershell
& work/baseline-env/Scripts/python.exe -B outputs/corrected_label_baseline/run_corrected_label_baseline.py
& work/baseline-env/Scripts/python.exe -B outputs/corrected_label_baseline/verify_corrected_label_baseline.py
```

Reruns regenerate only this experiment's outputs; they are reproductions, not new independent tests. The saved pipelines require features in inherited order with documented sentinels decoded to NaN. Only load trusted serialized models.
