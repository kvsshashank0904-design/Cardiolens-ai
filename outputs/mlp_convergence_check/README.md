# Experiment 4B reproduction

All new artifacts are confined to this directory. Experiment 3, Experiment 4, the source CSV and every older output are read-only dependencies. Their 85 pre-run output SHA-256 hashes and the source hash are in `mlp_convergence_config.json`.

Only max_iter changes, from 2000 to the predetermined 10000. max_fun remains 50000. Architecture, optimizer, tolerance, L2, seed, threshold, preprocessing, labels, groups and folds remain fixed. There is one new run, no retries and no search. Each fit starts afresh with seed 42. The two previous experiments are read as frozen references, never rerun.

## Review files

- `mlp_convergence_report.md`: optimization status, loss, full CV/holdout comparison, limitations.
- `mlp_convergence_metrics.json`: all folds, both evaluation views, denominators, confusion matrices, mean/sample SD, optimizer statuses and frozen references.
- `verification.json`: independent verification outcome, checks, errors and hashes.
- `run_mlp_convergence.py`: exact training/evaluation script, adapted into this new directory from the frozen Experiment 4 runner.
- `verify_mlp_convergence.py`: independent calculations and integrity/membership checks, adapted into this directory from the independent Experiment 4 verifier. It does not use the runner's metric formulas or fit models.
- `report_convergence.py`: report generation from saved metrics only.
- `mlp_convergence_config.json`, `configuration.json`: fixed configuration and run copy.
- `environment.json`, `requirements.txt`: runtime/dependency information. Python 3.12.10; pinned NumPy, SciPy, scikit-learn, joblib and threadpoolctl. Native fit threads limited to one.
- `execution.json`, `run_status.json`: fit order, group IDs, preprocessing state, warning text, optimization results and source integrity.
- `group_split_manifest.csv`: unchanged corrected group/partition/fold map copied for review.
- `cv_predictions.csv`, `cv_row_predictions.csv`, `test_predictions.csv`, `test_row_predictions.csv`: fixed-threshold predictions/probabilities and original row/physical-line links.
- `mlp_model.joblib`: final 241-development-group fitted pipeline, saved for audit rather than deployment. Load only this trusted model with the pinned dependencies.

## Verification without training

From the workspace root:

```powershell
& work/baseline-env/Scripts/python.exe -B outputs/mlp_convergence_check/verify_mlp_convergence.py
```

This regenerates only this experiment's verification.json. It recomputes saved metrics and manually calculates the saved network's probabilities for a serialization check, without fitting or tuning.

## Reproduce in a separate destination

Keep the original project layout and source path recorded in the configuration. The runner imports pure Experiment 3 helpers (which import the baseline metric helper), not prior mains. Frozen source evidence, manifests, configs, predictions and metrics must remain available; every dependency hash is listed in the configuration. No prior verification script is executed. A new reproduction destination must not already exist:

```powershell
& work/baseline-env/Scripts/python.exe -B outputs/mlp_convergence_check/run_mlp_convergence.py --output-dir outputs/mlp_convergence_reproduction
& work/baseline-env/Scripts/python.exe -B outputs/mlp_convergence_check/verify_mlp_convergence.py --results-dir outputs/mlp_convergence_reproduction
```

The runner refuses to overwrite completed results. Reproduction is not a new independent test. Numeric results may vary across platforms/BLAS versions; the environment is recorded. Use requirements.txt pins in Python 3.12.10 if rebuilding an environment. For a different source location, document a new configuration rather than silently modifying the frozen run.

## Saved model input contract

Thirteen columns in order: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal. Decode raw ca=4 and thal=0 to NaN before calling the pipeline; no other category remapping is used. Positive output class 1 is corrected UCI disease-presence coding. Threshold remains 0.5.

Convergence means recorded optimizer success, not global optimality or multi-seed stability. The holdout is previously inspected/shared. These outputs establish no clinical validity, diagnostic ability or patient-level generalization.
