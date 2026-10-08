# CardioLens AI baseline

Primary experiment: one representative per training feature group. Original CSV and every source-row mapping are preserved.

## Results

Selected **logistic_regression** by development-only mean five-fold ROC-AUC; seed 42, fixed threshold 0.5. No hyperparameter or threshold search.

| Candidate | Mean development ROC-AUC | Fold sample SD |
|---|---:|---:|
| majority | 0.500000 | 0.000000 |
| logistic_regression | 0.944755 | 0.026444 |

Only the selected model is scored on the final test. Fold SD is descriptive, not a confidence interval.

| Partition | Groups | Original rows | Group labels 0 / 1 | Row labels 0 / 1 |
|---|---:|---:|---|---|
| all | 302 | 1025 | 138 / 164 | 499 / 526 |
| development | 241 | 811 | 110 / 131 | 395 / 416 |
| test | 61 | 214 | 28 / 33 | 104 / 110 |

The requested 80/20 group split rounds to 241 development and 61 test groups. Row proportions differ because group multiplicities differ.

| Test view | N | Sensitivity | Specificity | Precision | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| distinct_group | 61 | 0.878788 | 0.642857 | 0.743590 | 0.805556 | 0.840909 |
| original_row_weighted | 214 | 0.872727 | 0.634615 | 0.716418 | 0.786885 | 0.838112 |

**distinct_group confusion matrix:** `[[18, 10], [4, 29]]`; rows=true 0/1, columns=predicted 0/1.
Metric denominators: `{'sensitivity': 33, 'specificity': 28, 'precision': 39, 'f1': 72, 'accuracy': 61, 'roc_auc_positive_negative_pairs': 924}`.

**original_row_weighted confusion matrix:** `[[66, 38], [14, 96]]`; rows=true 0/1, columns=predicted 0/1.
Metric denominators: `{'sensitivity': 110, 'specificity': 104, 'precision': 134, 'f1': 244, 'accuracy': 214, 'roc_auc_positive_negative_pairs': 11440}`.

The row-weighted view expands the same held-out group predictions back to their source rows; it does not retrain. These are test-subset results, not out-of-sample scores for all 1,025 rows. Repeated rows do not supply independent evidence.

## Methods and assumptions

Numeric/categorical roles are modeling assumptions, not verified feature definitions. Treat ca and slope as nominal, not ordinal; retain all observed codes including ca=4 and thal=0. Learn one-hot categories only on training groups, handle_unknown=ignore, drop=None. Standardize numeric features only on training groups. No imputation, feature selection, resampling, or label changes. Positive class is numeric target=1, whose clinical meaning remains unverified.

Group IDs hash ordered raw feature strings, excluding target. Numeric-normalized grouping was checked to agree. Representatives are first source occurrences; grouping collapses only the modeling view, never the CSV. CSV lines are physical, 1-based including the header; record numbers are logical data records after the header.

Groups sorted by ID are stratified 80/20 using seed 42. Development groups receive five fixed stratified folds. A fresh pipeline is fit for each candidate/fold. The majority classifier predicts the training majority; logistic regression uses L2 regularization with C=1. Categories and numeric scaling are learned inside each fit. Unseen category codes produce all-zero one-hot blocks. No imputation or category correction is performed.

The selection function receives only development features and labels. Test group IDs serve solely as an exclusion guard. Test labels are used for the initial requested stratification and final scoring, not model selection. The saved selection is hashed before test prediction and verified unchanged afterward. All fits record their group IDs in baseline_execution.json.

## Checks and limitations

All baseline runtime checks passed: complete row coverage; consistent group labels; zero train/validation/test overlap within each fold; no test group in selection or fits; one representative per training group; training-only scaler/category checks; one final test prediction call; unchanged source hash.

Source SHA-256 before and after: `ddb2996b2f4db2e00aad13f4518200179ff69f79093838e3c21ffa672ebec0f1`.

Dataset provenance, feature definitions/category codes, and target=1 semantics remain unverified. Sensitivity here means recall of numeric label 1; it is not established disease sensitivity. Feature groups are not patient identifiers. This educational experiment does not establish patient-level separation, clinical validity, diagnostic accuracy, or generalization to real patients. The small test set and unknown dependence limit conclusions; row weighting changes the estimand, not evidence strength. Test results must not drive further tuning on this same holdout.

Project context: MILF_Problem_Statements_Reference_Style (1).pdf p. 2, Problem Statement 3 describes the educational objective and metrics but supplies no verified codebook. Lightweight ML Primer for Freshers.pdf pp. 9-12 and 28-29 gives generic preprocessing/evaluation guidance; p. 39 describes the heart challenge. Neither resolves provenance or repetition.

Optional repetition-weighted training was not run. No UI was built.

The held-out group ROC-AUC (0.8409) is below the development mean (0.9448). This single small holdout gives a more cautious result; it was not used to revise encoding, model settings, threshold, or the split. The two scoring views are different weightings of the same predictions, not independent experiments.

## Execution and independent verification

Dependency setup initially failed with a temporary-directory permission error. Retrying with the required access succeeded in the workspace's isolated environment. Both candidates completed all five folds; the selected model completed the final development fit and held-out evaluation. No convergence error or unresolved execution failure occurred.

The separate verify_baseline.py script passed without retraining: it reconstructed all group IDs and row mappings from the source; reproduced split/fold assignments from the seed; checked fit membership and preprocessing traces; recomputed confusion matrices, ratios, and ROC-AUC independently; verified the frozen selection; and confirmed that an intentionally forbidden test-group fit is rejected before training. See baseline_verification.json for the saved result.

## Reproduce

Use Python 3.12 and the exact dependency versions in baseline_requirements.txt. From the workspace root:

```powershell
py -3.12 -m venv work/baseline-env
& work/baseline-env/Scripts/python.exe -m pip install -r outputs/baseline_requirements.txt
& work/baseline-env/Scripts/python.exe outputs/run_baseline.py --config outputs/baseline_config.json
& work/baseline-env/Scripts/python.exe outputs/verify_baseline.py
```

The source hash must match the approved audit; mismatches stop the run. Existing split assignments must match exactly. A rerun is reproduction, not a new independent test. Configuration, split, script hashes, versions, predictions, and metric denominators are saved. The serialized pipeline is baseline_model.joblib; load only trusted local model files.

Implementation references: [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html), [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).
