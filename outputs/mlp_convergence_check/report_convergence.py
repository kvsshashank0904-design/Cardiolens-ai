"""Render the Experiment 4B report from recorded results only."""
import json
from pathlib import Path

MEASURES=['sensitivity','specificity','precision','f1','accuracy','roc_auc']
VIEWS=['distinct_group','original_row_weighted']
MODELS=[('Experiment 3 logistic','reference'),('Experiment 4 MLP','frozen_mlp'),('Experiment 4B MLP','mlp')]

def write_report(out,m,c,events):
    fits=m['convergence'];cv=fits[:5]
    lines=['# Experiment 4B: MLP convergence and stability check','',
        '## Fixed design','',
        'Only max_iter changed: **2,000 -> 10,000**, predetermined before any new fit. Architecture remains Dense 32 ReLU -> Dense 16 ReLU -> one sigmoid. L-BFGS, L2 alpha=1, max_fun=50,000, tol=1e-5, seed=42, threshold=0.5 and all other explicit/default parameters are unchanged. No architecture, seed, threshold or regularization search; no retries. Every fit starts from the same seeded initialization methodology rather than warm-starting a previous model.', '',
        'Exact Experiment 3 corrected labels are reused: disease_present=1 = 1-original_target = int(matched UCI num>0). Local original target=1 corresponds to documented absence. ca=4 and thal=0 decode to NaN and then to the explicit missing category -1 before training-only one-hot encoding. Five numeric features use training-only StandardScaler; eight categorical features use the same nominal feature roles and unknown-category policy as Experiment 4. These modeling roles do not establish measurement validity.', '',
        'All 302 raw-feature group definitions, 241 development / 61 test assignments and five validation folds are reused without regeneration. Training uses one representative per group. The 1,025 source rows are untouched; repeated-row evaluation expands group predictions and is not independent evidence.', '',
        'Frozen references are read from ../corrected_label_baseline/corrected_label_metrics.json (explicit_missing) and ../model_comparison/model_comparison_metrics.json. Neither previous experiment was rerun. Source evidence remains ../dataset_investigation/record_correspondence.json and dataset_provenance_report.md.', '',
        '## Optimization results','',
        f"All five CV folds converged under the recorded optimizer stopping rule: **{m['all_five_cv_folds_converged']}**.", '',
        '| Fit | Iterations | Loss including L2 | Success / status | Function evaluations | Max absolute gradient | Warning count |',
        '|---|---:|---:|---|---:|---:|---:|']
    for e in fits:
        o=e['optimizer']
        lines.append(f"| {e['phase']} | {e['iterations']} | {e['training_loss_including_regularization']:.9f} | {o['success']} / {o['status']} | {o['nfev']} | {o['gradient_max_abs']:.8g} | {len(e['warnings'])} |")
        lines.append('') if False else None
    for e in fits:lines+=['',f"{e['phase']}: `{e['optimizer']['message']}`."]
    lines+=['','Success means scipy OptimizeResult success=true/status=0, not proof of a global minimum or satisfaction of the gradient tolerance specifically. L-BFGS can stop on relative objective reduction. The exact messages and gradients above make that distinction visible. A pass-through instrumentation wrapper records the optimizer result without changing arguments, callbacks or returned weights. The final training objective is available; sklearn L-BFGS does not expose an epoch loss curve here.','']
    oldevents=json.loads((Path(__file__).resolve().parent.parent/'model_comparison/execution.json').read_text())
    oldfits=[e for e in oldevents if 'fit_group_ids' in e]
    lines+=['| Fold | Experiment 4 iterations / loss | Experiment 4B iterations / loss |','|---|---|---|']
    for i,(a,b) in enumerate(zip(oldfits[:5],cv),1):
        lines.append(f"| {i} | {a['iterations']} / {a['training_loss_including_regularization']:.9f} | {b['iterations']} / {b['training_loss_including_regularization']:.9f} |")
    lines+=['','The original warnings in folds 2 and 3 are resolved in this fixed-seed run.' if m['all_five_cv_folds_converged'] else 'At least one CV fold still has no successful optimizer termination. The experiment stops at this predetermined allowance; no further tuning is attempted.', '',
        'Convergence across these folds is not multi-seed stability. This experiment does not measure variability across random initializations, new splits or new patients.', '',
        '## Counts','', '| Partition | Groups | Original rows | Group labels 0 / 1 | Row labels 0 / 1 |','|---|---:|---:|---|---|']
    for part,d in m['counts'].items():lines.append(f"| {part} | {d['group_count']} | {d['original_row_count']} | {d['group_class_counts']['0']} / {d['group_class_counts']['1']} | {d['row_class_counts']['0']} / {d['row_class_counts']['1']} |")
    lines+=['','## Development CV comparison','',
        'Each cell is mean (sample SD) over the five saved folds. SD describes fold variation; it is not a confidence interval. Frozen reference metrics are independently checked against their recorded predictions.','',
        '| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |','|---|---|---:|---:|---:|---:|---:|---:|']
    for name,key in MODELS:
        for v in VIEWS:
            d=m[key]['cv_summary_all_metrics'][v]
            lines.append('| '+name+' | '+v+' | '+' | '.join(f"{d[k]['mean']:.6f} ({d[k]['sample_sd']:.6f})" for k in MEASURES)+' |')
    lines+=['','### Experiment 4B individual CV folds','','| Fold / view | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC | Matrix [[TN,FP],[FN,TP]] |','|---|---:|---:|---:|---:|---:|---:|---|']
    for f in m['mlp']['cv_folds']:
        for v in VIEWS:
            d=f[v]
            lines.append('| '+str(f['fold'])+' / '+v+' | '+' | '.join(f'{d[k]:.6f}' for k in MEASURES)+f" | {d['confusion_matrix']} |")
    lines+=['','All fold counts, class counts and metric denominators are included in mlp_convergence_metrics.json. Each development group is validated exactly once.','']
    for name,key in MODELS:
        cm=np_sum_matrices([f['distinct_group']['confusion_matrix'] for f in m[key]['cv_folds']])
        lines.append(f"{name}: pooled development confusion matrix {cm}; {cm[1][0]} false negatives among 110 corrected-positive development groups.")
    lines+=['','## Previously inspected/shared holdout','',
        'One prespecified holdout prediction call follows all CV fits and the final 241-group fit. Results below are descriptive only and did not choose any settings. The verifier may independently calculate the same saved model probabilities; this is a serialization check, not a new model selection experiment.','',
        '| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC | Matrix [[TN,FP],[FN,TP]] |','|---|---|---:|---:|---:|---:|---:|---:|---|']
    for name,key in MODELS:
        for v in VIEWS:
            d=m[key]['test'][v]
            lines.append('| '+name+' | '+v+' | '+' | '.join(f'{d[k]:.6f}' for k in MEASURES)+f" | {d['confusion_matrix']} |")
    for v in VIEWS:lines+=['',f"4B {v} denominators: `{json.dumps(m['mlp']['test'][v]['denominators'])}`."]
    lines+=['','## Interpretation','']
    for key,label in [('reference','Experiment 3 logistic'),('frozen_mlp','Experiment 4 MLP')]:
        a=m[key]['cv_summary_all_metrics']['distinct_group'];b=m['mlp']['cv_summary_all_metrics']['distinct_group']
        lines.append(f"Compared with {label}, 4B development CV sensitivity changes from {a['sensitivity']['mean']:.6f} to {b['sensitivity']['mean']:.6f}, specificity from {a['specificity']['mean']:.6f} to {b['specificity']['mean']:.6f}, and AUC from {a['roc_auc']['mean']:.6f} to {b['roc_auc']['mean']:.6f}.")
    b=m['mlp']['cv_summary_all_metrics']['distinct_group'];a=m['reference']['cv_summary_all_metrics']['distinct_group']
    if b['sensitivity']['mean']<=a['sensitivity']['mean'] and b['roc_auc']['mean']<=a['roc_auc']['mean']:
        lines+=['','The convergence-checked MLP remains weaker than logistic regression on mean development sensitivity and ROC-AUC. There is no evidence here supporting replacement of logistic regression. Higher holdout sensitivity or F1 alone cannot establish superiority.']
    else:lines+=['','Some development measures improve, but this small, single-seed comparison cannot establish superiority. Examine sensitivity, false negatives, specificity and AUC jointly rather than selecting a winner by holdout results.']
    lines+=['','The larger optimization allowance is informative about the two warnings. It is not, by itself, a reason for further architecture or threshold tuning. A separate, prespecified multi-seed development-only study could address initialization stability if educational interest warrants it; none is performed or selected here.', '',
        'The shared holdout was previously inspected. No independent test-performance, diagnostic, clinical-validity or patient-generalization claim follows. Acquisition/transformation/repetition history, missingness mechanism, some units, the omitted UCI record and patient identities remain unresolved. Numerical convergence does not resolve those limitations. No SNN, extra hidden layers or UI are part of this experiment.', '',
        '## Verification and reproduction','',
        f"The runner checks the source SHA-256 and {len(c['protected_sha256'])} frozen output hashes before and after. The independent verifier checks the same groups/folds, zero train-validation-test overlap, all preprocessing statistics, unchanged defaults except max_iter, all model metrics via independent counts/pairwise AUC, and the final saved network forward calculation. Consult verification.json for actual PASS/FAIL status and errors; completing the runner alone is not verification.", '',
        'README.md contains exact reproduction commands, pinned dependencies and the complete artifact inventory. Reproduction must use a fresh output directory. Earlier experiment mains are never called, and Python bytecode writing is disabled.']
    (out/'mlp_convergence_report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def np_sum_matrices(matrices):
    return [[sum(m[i][j] for m in matrices) for j in range(2)] for i in range(2)]
