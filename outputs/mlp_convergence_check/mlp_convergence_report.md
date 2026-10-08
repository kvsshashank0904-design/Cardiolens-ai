# Experiment 4B: MLP convergence and stability check

## Fixed design

Only max_iter changed: **2,000 -> 10,000**, predetermined before any new fit. Architecture remains Dense 32 ReLU -> Dense 16 ReLU -> one sigmoid. L-BFGS, L2 alpha=1, max_fun=50,000, tol=1e-5, seed=42, threshold=0.5 and all other explicit/default parameters are unchanged. No architecture, seed, threshold or regularization search; no retries. Every fit starts from the same seeded initialization methodology rather than warm-starting a previous model.

Exact Experiment 3 corrected labels are reused: disease_present=1 = 1-original_target = int(matched UCI num>0). Local original target=1 corresponds to documented absence. ca=4 and thal=0 decode to NaN and then to the explicit missing category -1 before training-only one-hot encoding. Five numeric features use training-only StandardScaler; eight categorical features use the same nominal feature roles and unknown-category policy as Experiment 4. These modeling roles do not establish measurement validity.

All 302 raw-feature group definitions, 241 development / 61 test assignments and five validation folds are reused without regeneration. Training uses one representative per group. The 1,025 source rows are untouched; repeated-row evaluation expands group predictions and is not independent evidence.

Frozen references are read from ../corrected_label_baseline/corrected_label_metrics.json (explicit_missing) and ../model_comparison/model_comparison_metrics.json. Neither previous experiment was rerun. Source evidence remains ../dataset_investigation/record_correspondence.json and dataset_provenance_report.md.

## Optimization results

All five CV folds converged under the recorded optimizer stopping rule: **True**.

| Fit | Iterations | Loss including L2 | Success / status | Function evaluations | Max absolute gradient | Warning count |
|---|---:|---:|---|---:|---:|---:|
| cv_fit_1 | 1205 | 0.095872466 | True / 0 | 1284 | 0.005341381 | 0 |
| cv_fit_2 | 3243 | 0.100773921 | True / 0 | 3439 | 0.0039866569 | 0 |
| cv_fit_3 | 2634 | 0.096334741 | True / 0 | 2778 | 0.004740825 | 0 |
| cv_fit_4 | 1443 | 0.090048438 | True / 0 | 1507 | 0.0036676037 | 0 |
| cv_fit_5 | 1225 | 0.096574147 | True / 0 | 1298 | 0.0057284104 | 0 |
| final_development_fit | 943 | 0.088784230 | True / 0 | 1001 | 0.0039435188 | 0 |

cv_fit_1: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

cv_fit_2: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

cv_fit_3: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

cv_fit_4: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

cv_fit_5: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

final_development_fit: `CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH`.

Success means scipy OptimizeResult success=true/status=0, not proof of a global minimum or satisfaction of the gradient tolerance specifically. L-BFGS can stop on relative objective reduction. The exact messages and gradients above make that distinction visible. A pass-through instrumentation wrapper records the optimizer result without changing arguments, callbacks or returned weights. The final training objective is available; sklearn L-BFGS does not expose an epoch loss curve here.

| Fold | Experiment 4 iterations / loss | Experiment 4B iterations / loss |
|---|---|---|
| 1 | 1205 / 0.095872466 | 1205 / 0.095872466 |
| 2 | 2000 / 0.100933356 | 3243 / 0.100773921 |
| 3 | 2000 / 0.096401789 | 2634 / 0.096334741 |
| 4 | 1443 / 0.090048438 | 1443 / 0.090048438 |
| 5 | 1225 / 0.096574147 | 1225 / 0.096574147 |

The original warnings in folds 2 and 3 are resolved in this fixed-seed run.

Convergence across these folds is not multi-seed stability. This experiment does not measure variability across random initializations, new splits or new patients.

## Counts

| Partition | Groups | Original rows | Group labels 0 / 1 | Row labels 0 / 1 |
|---|---:|---:|---|---|
| all | 302 | 1025 | 164 / 138 | 526 / 499 |
| development | 241 | 811 | 131 / 110 | 416 / 395 |
| test | 61 | 214 | 33 / 28 | 110 / 104 |

## Development CV comparison

Each cell is mean (sample SD) over the five saved folds. SD describes fold variation; it is not a confidence interval. Frozen reference metrics are independently checked against their recorded predictions.

| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| Experiment 3 logistic | distinct_group | 0.854545 (0.098543) | 0.885755 (0.080955) | 0.870709 (0.081201) | 0.857566 (0.054287) | 0.871259 (0.050014) | 0.944755 (0.026444) |
| Experiment 3 logistic | original_row_weighted | 0.854315 (0.112241) | 0.888620 (0.076175) | 0.886509 (0.067758) | 0.865009 (0.060423) | 0.872238 (0.054975) | 0.945624 (0.028318) |
| Experiment 4 MLP | distinct_group | 0.809091 (0.103652) | 0.809402 (0.075943) | 0.788465 (0.057173) | 0.792681 (0.030864) | 0.809014 (0.018672) | 0.903846 (0.019856) |
| Experiment 4 MLP | original_row_weighted | 0.803380 (0.118146) | 0.805752 (0.080560) | 0.804390 (0.054804) | 0.797131 (0.044942) | 0.804932 (0.026353) | 0.903501 (0.022027) |
| Experiment 4B MLP | distinct_group | 0.809091 (0.103652) | 0.817094 (0.067462) | 0.794163 (0.052453) | 0.796082 (0.034806) | 0.813180 (0.021720) | 0.902797 (0.019802) |
| Experiment 4B MLP | original_row_weighted | 0.803380 (0.118146) | 0.812895 (0.071496) | 0.809194 (0.049966) | 0.799975 (0.047512) | 0.808591 (0.028578) | 0.902516 (0.021862) |

### Experiment 4B individual CV folds

| Fold / view | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC | Matrix [[TN,FP],[FN,TP]] |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 / distinct_group | 0.909091 | 0.777778 | 0.769231 | 0.833333 | 0.836735 | 0.909091 | [[21, 6], [2, 20]] |
| 1 / original_row_weighted | 0.914634 | 0.783133 | 0.806452 | 0.857143 | 0.848485 | 0.915810 | [[65, 18], [7, 75]] |
| 2 / distinct_group | 0.909091 | 0.769231 | 0.769231 | 0.833333 | 0.833333 | 0.931818 | [[20, 6], [2, 20]] |
| 2 / original_row_weighted | 0.912500 | 0.750000 | 0.776596 | 0.839080 | 0.829268 | 0.933036 | [[63, 21], [7, 73]] |
| 3 / distinct_group | 0.727273 | 0.846154 | 0.800000 | 0.761905 | 0.791667 | 0.888112 | [[22, 4], [6, 16]] |
| 3 / original_row_weighted | 0.723684 | 0.840909 | 0.797101 | 0.758621 | 0.786585 | 0.888457 | [[74, 14], [21, 55]] |
| 4 / distinct_group | 0.681818 | 0.923077 | 0.882353 | 0.769231 | 0.812500 | 0.903846 | [[24, 2], [7, 15]] |
| 4 / original_row_weighted | 0.645570 | 0.925000 | 0.894737 | 0.750000 | 0.786164 | 0.896677 | [[74, 6], [28, 51]] |
| 5 / distinct_group | 0.818182 | 0.769231 | 0.750000 | 0.782609 | 0.791667 | 0.881119 | [[20, 6], [4, 18]] |
| 5 / original_row_weighted | 0.820513 | 0.765432 | 0.771084 | 0.795031 | 0.792453 | 0.878601 | [[62, 19], [14, 64]] |

All fold counts, class counts and metric denominators are included in mlp_convergence_metrics.json. Each development group is validated exactly once.

Experiment 3 logistic: pooled development confusion matrix [[116, 15], [16, 94]]; 16 false negatives among 110 corrected-positive development groups.
Experiment 4 MLP: pooled development confusion matrix [[106, 25], [21, 89]]; 21 false negatives among 110 corrected-positive development groups.
Experiment 4B MLP: pooled development confusion matrix [[107, 24], [21, 89]]; 21 false negatives among 110 corrected-positive development groups.

## Previously inspected/shared holdout

One prespecified holdout prediction call follows all CV fits and the final 241-group fit. Results below are descriptive only and did not choose any settings. The verifier may independently calculate the same saved model probabilities; this is a serialization check, not a new model selection experiment.

| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC | Matrix [[TN,FP],[FN,TP]] |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Experiment 3 logistic | distinct_group | 0.642857 | 0.878788 | 0.818182 | 0.720000 | 0.770492 | 0.840909 | [[29, 4], [10, 18]] |
| Experiment 3 logistic | original_row_weighted | 0.634615 | 0.872727 | 0.825000 | 0.717391 | 0.757009 | 0.838112 | [[96, 14], [38, 66]] |
| Experiment 4 MLP | distinct_group | 0.714286 | 0.818182 | 0.769231 | 0.740741 | 0.770492 | 0.817100 | [[27, 6], [8, 20]] |
| Experiment 4 MLP | original_row_weighted | 0.701923 | 0.818182 | 0.784946 | 0.741117 | 0.761682 | 0.816434 | [[90, 20], [31, 73]] |
| Experiment 4B MLP | distinct_group | 0.714286 | 0.818182 | 0.769231 | 0.740741 | 0.770492 | 0.817100 | [[27, 6], [8, 20]] |
| Experiment 4B MLP | original_row_weighted | 0.701923 | 0.818182 | 0.784946 | 0.741117 | 0.761682 | 0.816434 | [[90, 20], [31, 73]] |

4B distinct_group denominators: `{"sensitivity": 28, "specificity": 33, "precision": 26, "f1": 54, "accuracy": 61, "roc_auc_positive_negative_pairs": 924}`.

4B original_row_weighted denominators: `{"sensitivity": 104, "specificity": 110, "precision": 93, "f1": 197, "accuracy": 214, "roc_auc_positive_negative_pairs": 11440}`.

## Interpretation

Compared with Experiment 3 logistic, 4B development CV sensitivity changes from 0.854545 to 0.809091, specificity from 0.885755 to 0.817094, and AUC from 0.944755 to 0.902797.
Compared with Experiment 4 MLP, 4B development CV sensitivity changes from 0.809091 to 0.809091, specificity from 0.809402 to 0.817094, and AUC from 0.903846 to 0.902797.

The convergence-checked MLP remains weaker than logistic regression on mean development sensitivity and ROC-AUC. There is no evidence here supporting replacement of logistic regression. Higher holdout sensitivity or F1 alone cannot establish superiority.

The larger optimization allowance is informative about the two warnings. It is not, by itself, a reason for further architecture or threshold tuning. A separate, prespecified multi-seed development-only study could address initialization stability if educational interest warrants it; none is performed or selected here.

The shared holdout was previously inspected. No independent test-performance, diagnostic, clinical-validity or patient-generalization claim follows. Acquisition/transformation/repetition history, missingness mechanism, some units, the omitted UCI record and patient identities remain unresolved. Numerical convergence does not resolve those limitations. No SNN, extra hidden layers or UI are part of this experiment.

## Verification and reproduction

The runner checks the source SHA-256 and 85 frozen output hashes before and after. The independent verifier checks the same groups/folds, zero train-validation-test overlap, all preprocessing statistics, unchanged defaults except max_iter, all model metrics via independent counts/pairwise AUC, and the final saved network forward calculation. Consult verification.json for actual PASS/FAIL status and errors; completing the runner alone is not verification.

README.md contains exact reproduction commands, pinned dependencies and the complete artifact inventory. Reproduction must use a fresh output directory. Earlier experiment mains are never called, and Python bytecode writing is disabled.
