# Experiment 4: controlled neural network comparison

**Review conclusion:** This run does not establish a useful overall improvement over the frozen logistic baseline. On the previously inspected holdout the MLP improves positive sensitivity and F1, but loses specificity, precision and ROC-AUC. Development CV sensitivity and AUC are lower. Retain logistic regression as the comparison reference; these results do not justify replacing it for frontend integration.

**Execution limitation:** CV folds 2 and 3 reached the prespecified 2,000-iteration limit and emitted ConvergenceWarning. Their metrics describe the fitted weights at that limit; optimization convergence was not established. The other three CV fits and the final fit emitted no warnings (final fit: 943 iterations). No configurations were changed, no fits were retried and no threshold tuning occurred after observing results. All six fits completed, but this was not six converged fits.

**Verification:** PASS_WITH_WARNINGS, with no integrity, metric or group-separation errors. Source CSV and all 67 pre-existing output files, including the 18 Experiment 3 artifacts, retain their original hashes. See verification.json for the actual checks and full warning text. The runner's run_status.json status PASS means execution completed; its warnings array records the two nonconverged fits. It is not a claim of warning-free convergence.

This is a prespecified small MLP compared with the frozen Experiment 3 **explicit_missing** logistic baseline. Logistic regression was not refitted. Its alternative mode-plus-indicator pipeline was not selected as a comparator after seeing results.

## Design and evidence

Corrected positive class: disease_present=1 = 1-original_target = int(matched UCI num>0). Original target=1 corresponds to documented absence. All 302 record correspondences were checked again against the pinned UCI evidence. Local ca=4 and thal=0 decode to NaN, then to an explicit missing category (-1) inside the pipeline. No source row or label was changed.

Evidence and preserved dependencies: ../corrected_label_baseline/corrected_label_report.md, corrected_label_config.json, corrected_group_manifest.csv and run_corrected_label_baseline.py; ../dataset_investigation/record_correspondence.json and dataset_provenance_report.md. These establish record correspondence, not the historical transformation author's intent.

Five numeric features are standardized; eight nominal features use constant missing fill and one-hot encoding with unknown categories ignored. Numeric/categorical roles remain modeling assumptions. Every fold constructs a fresh preprocessing pipeline and fits it only on its training groups. Sentinel decoding is a fixed evidence-based transformation. The saved model expects 13 columns in inherited feature order with ca=4/thal=0 already decoded to NaN.

Fixed MLP: Dense 32 ReLU -> Dense 16 ReLU -> one sigmoid output; binary log loss with L2 alpha=1.0, L-BFGS, max_iter=2000, max_fun=50000, tol=1e-5, seed=42, threshold=0.5, no class/sample weights. L-BFGS is a full-batch optimizer; it uses training-objective convergence, not validation early stopping. L2 was set before this run. No hyperparameter, seed, epoch, threshold, or preprocessing search was performed. Architecture/parameters are also recorded in configuration.json and execution.json.

The exact saved development/test assignment and five folds are reused; no split is regenerated. Training uses one representative per feature group. The original 1,025 rows remain intact. Row-weighted evaluation maps the same group predictions back to all corresponding source rows; it is not a second independent sample.

## Counts

| Partition | Groups | Original rows | Group class 0 / 1 | Row class 0 / 1 |
|---|---:|---:|---|---|
| all | 302 | 1025 | 164 / 138 | 526 / 499 |
| development | 241 | 811 | 131 / 110 | 416 / 395 |
| test | 61 | 214 | 33 / 28 | 110 / 104 |

## Development-only five-fold results

Means and sample SD across folds are descriptive, not confidence intervals. All six metrics, per-fold denominators, confusion matrices and pooled MLP out-of-fold metrics are in the JSON. Pooled metrics are not averaged fold metrics.

| Model | View | Sensitivity mean (SD) | AUC mean (SD) |
|---|---|---:|---:|
| Frozen logistic | distinct_group | 0.854545 (0.098543) | 0.944755 (0.026444) |
| Frozen logistic | original_row_weighted | 0.854315 (0.112241) | 0.945624 (0.028318) |
| MLP | distinct_group | 0.809091 (0.103652) | 0.903846 (0.019856) |
| MLP | original_row_weighted | 0.803380 (0.118146) | 0.903501 (0.022027) |

## Previously inspected holdout

| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| Frozen logistic | distinct_group | 0.642857 | 0.878788 | 0.818182 | 0.720000 | 0.770492 | 0.840909 |
| Frozen logistic | original_row_weighted | 0.634615 | 0.872727 | 0.825000 | 0.717391 | 0.757009 | 0.838112 |
| MLP | distinct_group | 0.714286 | 0.818182 | 0.769231 | 0.740741 | 0.770492 | 0.817100 |
| MLP | original_row_weighted | 0.701923 | 0.818182 | 0.784946 | 0.741117 | 0.761682 | 0.816434 |

reference, distinct_group: matrix **[[29, 4], [10, 18]]**; denominators `{"sensitivity": 28, "specificity": 33, "precision": 22, "f1": 50, "accuracy": 61, "roc_auc_positive_negative_pairs": 924}`.

reference, original_row_weighted: matrix **[[96, 14], [38, 66]]**; denominators `{"sensitivity": 104, "specificity": 110, "precision": 80, "f1": 184, "accuracy": 214, "roc_auc_positive_negative_pairs": 11440}`.

mlp, distinct_group: matrix **[[27, 6], [8, 20]]**; denominators `{"sensitivity": 28, "specificity": 33, "precision": 26, "f1": 54, "accuracy": 61, "roc_auc_positive_negative_pairs": 924}`.

mlp, original_row_weighted: matrix **[[90, 20], [31, 73]]**; denominators `{"sensitivity": 104, "specificity": 110, "precision": 93, "f1": 197, "accuracy": 214, "roc_auc_positive_negative_pairs": 11440}`.

Matrices are [[TN, FP], [FN, TP]], true labels in rows and predictions in columns. Positive means the corrected UCI presence class. Undefined rates use null.

## Interpretation

distinct_group: MLP false negatives 8 versus logistic 10, among 28 corrected positives. Improved observed metrics: sensitivity, f1. Lower observed metrics: specificity, precision, roc_auc. Exact differences are in the metrics JSON.
original_row_weighted: MLP false negatives 31 versus logistic 38, among 104 corrected positives. Improved observed metrics: sensitivity, f1, accuracy. Lower observed metrics: specificity, precision, roc_auc. Exact differences are in the metrics JSON.

These are descriptive comparisons of one prespecified network/seed, not proof of statistically reliable improvement. Sensitivity and false negatives must be assessed alongside specificity and AUC; accuracy alone is insufficient. The holdout was previously inspected in multiple experiments and provenance analysis. It is not independent test performance, even though it enters no fitting, preprocessing, stopping decision or tuning in this run.

Patient identifiers and patient independence are unknown. Acquisition route, repetition rationale, transformation history, the omitted upstream record, missingness mechanism and some units remain unresolved. Feature groups are not patient identities, and repeated rows do not increase independent evidence. No clinical validity, diagnostic ability or patient-level generalization is established. No UI was built.

## Integrity and reproduction

The runner checked the original source hash and all 67 pre-existing output files before and after training. Execution records contain all training group IDs and fitted preprocessing statistics. All six fit warning lists are saved. See verification.json for independent metric and structural checks; the runner does not substitute for that verifier.

See README.md for pinned dependencies, read-only verification and reproduction into a separate new directory. The reference helpers are imported with bytecode writing disabled; none of their experiment entry points run. All new outputs are confined to this experiment directory.
