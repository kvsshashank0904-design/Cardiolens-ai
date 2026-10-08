# CardioLens AI Experiment 2: repetition-weighted training

**Secondary exploratory evaluation on a previously inspected holdout.** These experiments share the same 61 test feature groups and are not independent evaluations.

Only training-row inclusion changes: Experiment 1 fits one representative per group; Experiment 2 fits every original eligible row once. Both use the saved split and five folds, seed 42, fixed logistic regression (L2, C=1), identical preprocessing choices, and threshold 0.5. No model selection or tuning occurs in Experiment 2.

## Training counts

| Stage | Groups (both) | Experiment 1 training rows | Experiment 2 training rows | Validation groups / original rows |
|---|---:|---:|---:|---|
| Fold 1 | 192 | 192 | 646 | 49 / 165 |
| Fold 2 | 193 | 193 | 647 | 48 / 164 |
| Fold 3 | 193 | 193 | 647 | 48 / 164 |
| Fold 4 | 193 | 193 | 652 | 48 / 159 |
| Fold 5 | 193 | 193 | 652 | 48 / 159 |
| Final development fit | 241 | 241 | 811 | Test: 61 / 214 |

Development class counts: 110 label-0 / 131 label-1 groups; 395 label-0 / 416 label-1 original rows. Test: 28 label-0 / 33 label-1 groups; 104 label-0 / 110 label-1 rows. Full per-fold counts are saved in the CV metrics.

## Development cross-validation

| View | Exp. 1 mean AUC | Exp. 1 fold SD | Exp. 2 mean AUC | Exp. 2 fold SD | Signed mean difference | Absolute mean difference | Absolute SD difference |
|---|---:|---:|---:|---:|---:|---:|---:|
| distinct_group | 0.944755 | 0.026444 | 0.942657 | 0.029081 | -0.002098 | 0.002098 | 0.002637 |
| original_row_weighted | 0.945624 | 0.028318 | 0.943218 | 0.031079 | -0.002406 | 0.002406 | 0.002761 |

Means are unweighted means of five fold AUCs; SD is sample SD (ddof=1), not a confidence interval. Experiment 1 row-weighted CV metrics were reconstructed from its saved logistic-regression out-of-fold predictions and original multiplicities; the primary model was not rerun or modified.

## Shared final holdout

| View | Metric | Experiment 1 | Experiment 2 | Signed difference (2 minus 1) | Absolute difference |
|---|---|---:|---:|---:|---:|
| distinct_group | roc_auc | 0.840909 | 0.839827 | -0.001082 | 0.001082 |
| distinct_group | sensitivity | 0.878788 | 0.848485 | -0.030303 | 0.030303 |
| distinct_group | specificity | 0.642857 | 0.642857 | +0.000000 | 0.000000 |
| distinct_group | precision | 0.743590 | 0.736842 | -0.006748 | 0.006748 |
| distinct_group | f1 | 0.805556 | 0.788732 | -0.016823 | 0.016823 |
| distinct_group | accuracy | 0.770492 | 0.754098 | -0.016393 | 0.016393 |
| original_row_weighted | roc_auc | 0.838112 | 0.837325 | -0.000787 | 0.000787 |
| original_row_weighted | sensitivity | 0.872727 | 0.845455 | -0.027273 | 0.027273 |
| original_row_weighted | specificity | 0.634615 | 0.634615 | +0.000000 | 0.000000 |
| original_row_weighted | precision | 0.716418 | 0.709924 | -0.006494 | 0.006494 |
| original_row_weighted | f1 | 0.786885 | 0.771784 | -0.015101 | 0.015101 |
| original_row_weighted | accuracy | 0.757009 | 0.742991 | -0.014019 | 0.014019 |

**distinct_group:** Experiment 1 confusion matrix `[[18, 10], [4, 29]]`; Experiment 2 `[[18, 10], [5, 28]]`. Rows=true [0,1], columns=predicted [0,1].
Experiment 2 metric denominators: `{'sensitivity': 33, 'specificity': 28, 'precision': 38, 'f1': 71, 'accuracy': 61, 'roc_auc_positive_negative_pairs': 924}`.

**original_row_weighted:** Experiment 1 confusion matrix `[[66, 38], [14, 96]]`; Experiment 2 `[[66, 38], [17, 93]]`. Rows=true [0,1], columns=predicted [0,1].
Experiment 2 metric denominators: `{'sensitivity': 110, 'specificity': 104, 'precision': 131, 'f1': 241, 'accuracy': 214, 'roc_auc_positive_negative_pairs': 11440}`.

## Interpretation and limits

Observed result: Experiment 2's mean development ROC-AUC is lower by 0.002098 in the distinct-group view and 0.002406 in the original-row-weighted view. Shared-test ROC-AUC is lower by 0.001082 and 0.000787 respectively. At the fixed threshold, numeric-label-1 false negatives increase from 4 to 5 groups (14 to 17 original rows); specificity is unchanged. These descriptive differences are not evidence of statistical significance or erroneous repetition.

The comparison measures how observed repetition frequencies affect this pipeline on this split. The expanded data changes the numeric scaler statistics and the contribution of records to logistic-regression fitting. With C held fixed, changing total training sample count can also change the balance of data loss and regularization; this is not solely a comparison of relative group weights.

A higher score would not establish a superior model; a lower score would not establish erroneous repetitions. No statistical-significance claim is made. Repeated rows are neither independent patients nor independent evidence. Small, previously inspected test data and unknown data generation limit interpretation. No test result was used to revise the experiment.

Dataset provenance, feature definitions/category codes, and target=1 semantics remain unverified. Sensitivity is recall of numeric label 1. Groups represent identical features, not patient identities. The comparison establishes no patient-level independence, clinical validity, diagnostic accuracy, or generalization to new patients.

Encoding assumptions are inherited: age, trestbps, chol, thalach, oldpeak standardized; sex, cp, fbs, restecg, exang, slope, ca, thal one-hot encoded as nominal categories with unknown categories ignored. ca=4 and thal=0 remain unchanged. The scaler learns from expanded training rows; the encoder learns only categories present in those rows. No imputation or label alteration.

## Verification and reproduction

Execution status: **PASS**. All five expanded-row CV fits and the final 811-row development fit completed with no convergence errors. Independent verification status: **PASS**, with an empty errors list. The source CSV and all 23 protected primary files remained byte-for-byte unchanged. No unresolved failure occurred in this experiment.

The runner checks source/primary hashes before and after execution and logs every fitting source-row number, group, multiplicity, scaler statistics, and category set. The separate verification script independently checks predictions, metric denominators, confusion matrices, pairwise AUCs, and training membership. Its authoritative result is repetition_weighted_verification.json.

From the workspace root, using the primary pinned environment:

```powershell
& work/baseline-env/Scripts/python.exe -B outputs/repetition_weighted/run_repetition_weighted.py
& work/baseline-env/Scripts/python.exe -B outputs/repetition_weighted/verify_repetition_weighted.py
```

Configuration contains the inherited settings and pre-experiment hashes of all primary files. Primary helpers are imported read-only with bytecode writes disabled. Environment and script hashes are saved. Rerunning reproduces the same exploratory evaluation; it is not a fresh holdout. No UI is created.
