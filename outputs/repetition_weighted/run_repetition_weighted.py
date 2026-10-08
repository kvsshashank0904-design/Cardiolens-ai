"""Frozen secondary experiment. No primary artifact is written or refit.
Run: work/baseline-env/Scripts/python.exe -B outputs/repetition_weighted/run_repetition_weighted.py
"""
import sys
sys.dont_write_bytecode = True
import csv
import hashlib
import json
import platform
import warnings
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
import scipy
import sklearn
import threadpoolctl
from sklearn.exceptions import ConvergenceWarning

OUT = Path(__file__).resolve().parent
PRIMARY = OUT.parent
sys.path.insert(0, str(PRIMARY))
# These pure helpers are shared with Experiment 1; its main() is never called.
from run_baseline import make_model, score, predict, require, dump, write_csv


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def check_frozen(design):
    errors = []
    for name, expected in design['primary_file_sha256'].items():
        path = PRIMARY / name
        if not path.is_file() or sha(path) != expected:
            errors.append('Primary artifact changed: ' + name)
    source = Path(design['primary_config']['source_path'])
    if sha(source) != design['source_sha256']:
        errors.append('Source hash mismatch')
    require(not errors, '; '.join(errors))


def inputs(design):
    check_frozen(design)
    cfg = design['primary_config']
    require(cfg == load_json(PRIMARY/'baseline_config.json'), 'Configuration differs from primary')
    require(cfg['threshold'] == 0.5 and design['model'] == 'logistic_regression', 'Design not fixed')
    source = read_csv(Path(cfg['source_path']))
    manifest = read_csv(PRIMARY/'group_manifest.csv')
    split_list = read_csv(PRIMARY/'group_split.csv')
    groups = {r['group_id']: r for r in split_list}
    require(len(groups) == len(split_list) == cfg['expected_groups'], 'Unexpected or duplicate groups')
    require(len(source) == len(manifest) == cfg['expected_rows'], 'Incomplete source mapping')
    rows = []
    for n, (record, mapping) in enumerate(zip(source, manifest), 1):
        gid = mapping['group_id']
        key = [cfg['features'], [record[f] for f in cfg['features']]]
        calculated = hashlib.sha256(json.dumps(key, separators=(',', ':')).encode()).hexdigest()
        require(gid == calculated and int(mapping['record_number']) == n, 'Incorrect row/group mapping')
        group = groups[gid]
        require(record['target'] == mapping['target'] == group['target'], 'Conflicting or changed label')
        require(all(record[f] == group[f] for f in cfg['features']), 'Group features differ')
        require(all(mapping[f] == group[f] for f in ['partition', 'validation_fold']), 'Saved assignments disagree')
        rows.append({**record, **mapping})
    require(Counter(r['group_id'] for r in rows) == Counter({g:int(v['original_row_count']) for g,v in groups.items()}), 'Multiplicity mismatch')
    return cfg, rows, groups


def count_groups(ids, rows, groups):
    selected = [r for r in rows if r['group_id'] in set(ids)]
    return {'groups': len(ids), 'original_rows': len(selected),
            'group_class_counts': {str(c): sum(int(groups[g]['target']) == c for g in ids) for c in (0,1)},
            'row_class_counts': {str(c): sum(int(r['target']) == c for r in selected) for c in (0,1)}}


def fit_expanded(train_rows, eligible_groups, forbidden_groups, cfg, phase, events):
    ids = [r['group_id'] for r in train_rows]
    ordinals = [int(r['record_number']) for r in train_rows]
    require(set(ids) == set(eligible_groups), 'Training group membership mismatch')
    require(not set(ids) & set(forbidden_groups), 'Validation/test group in training')
    require(len(ordinals) == len(set(ordinals)), 'A source row was included more than once')
    X = np.array([[float(r[f]) for f in cfg['features']] for r in train_rows])
    y = np.array([int(r['target']) for r in train_rows])
    model = make_model('logistic_regression', cfg)
    with warnings.catch_warnings():
        warnings.simplefilter('error', ConvergenceWarning)
        model.fit(X, y)
    prep = model.named_steps['preprocess']
    scaler = prep.named_transformers_['numeric']
    encoder = prep.named_transformers_['categorical']
    ni = [cfg['features'].index(f) for f in cfg['numeric_features']]
    ci = [cfg['features'].index(f) for f in cfg['categorical_features']]
    require(int(scaler.n_samples_seen_) == len(train_rows), 'Wrong scaler fitting count')
    require(np.allclose(scaler.mean_, X[:,ni].mean(axis=0)) and np.allclose(scaler.var_, X[:,ni].var(axis=0)), 'Scaler does not reflect expanded training rows')
    require(all(np.array_equal(v, np.unique(X[:,i])) for v,i in zip(encoder.categories_,ci)), 'Encoder category mismatch')
    events.append({'phase': phase, 'model': 'logistic_regression',
        'training_group_ids': sorted(eligible_groups), 'training_record_numbers': ordinals,
        'training_row_count': len(train_rows), 'training_group_count': len(eligible_groups),
        'group_multiplicities': dict(sorted(Counter(ids).items())),
        'training_class_counts': {str(c): int(sum(y == c)) for c in (0,1)},
        'scaler_n_samples_seen': int(scaler.n_samples_seen_), 'scaler_mean': scaler.mean_.tolist(),
        'scaler_variance': scaler.var_.tolist(),
        'learned_categories': {f:v.tolist() for f,v in zip(cfg['categorical_features'],encoder.categories_)},
        'model_parameters': model.named_steps['model'].get_params(),
        'iterations': model.named_steps['model'].n_iter_.tolist(),
        'training_data_sha256': hashlib.sha256(json.dumps({'X':X.tolist(),'y':y.tolist(),'records':ordinals},separators=(',',':')).encode()).hexdigest()})
    return model


def predict_groups(model, ids, groups, cfg, fold, events):
    ids = sorted(ids)
    require(len(ids) == len(set(ids)), 'Prediction must contain one row per group')
    X = np.array([[float(groups[g][f]) for f in cfg['features']] for g in ids])
    predicted, probabilities = predict(model, X, cfg)
    events.append({'phase': 'test_prediction' if fold == 0 else 'validation_prediction',
                   'fold': fold, 'group_ids': ids, 'prediction_calls': 1})
    return [{'fold': fold, 'group_id':g, 'target':int(groups[g]['target']),
             'prediction':int(p), 'probability_target_1':float(q),
             'original_row_count':int(groups[g]['original_row_count'])}
            for g,p,q in zip(ids,predicted,probabilities)]


def expand_predictions(predictions, rows):
    lookup = {r['group_id']:r for r in predictions}
    return [{k:r[k] for k in ['record_number','csv_line_start','csv_line_end','group_id']} |
            {k:lookup[r['group_id']][k] for k in ['fold','target','prediction','probability_target_1']}
            for r in rows if r['group_id'] in lookup]


def evaluate(predictions):
    return score(np.array([int(r['target']) for r in predictions]),
                 np.array([int(r['prediction']) for r in predictions]),
                 np.array([float(r['probability_target_1']) for r in predictions]))


def summary(folds):
    return {view:{'mean_roc_auc':float(np.mean([f[view]['roc_auc'] for f in folds])),
                  'sample_sd_roc_auc':float(np.std([f[view]['roc_auc'] for f in folds],ddof=1))}
            for view in ['distinct_group','original_row_weighted']}


def comparison(metrics, cv, rows, groups):
    primary = load_json(PRIMARY/'baseline_metrics.json')
    require(primary['selected_model'] == 'logistic_regression', 'Primary comparator is not logistic regression')
    old_predictions = [r for r in read_csv(PRIMARY/'cv_predictions.csv') if r['candidate'] == 'logistic_regression']
    derived = []
    for f in range(1,6):
        p = [r for r in old_predictions if int(r['fold']) == f]
        derived.append({'fold':f,'distinct_group':evaluate(p),'original_row_weighted':evaluate(expand_predictions(p,rows))})
    primary_cv = summary(derived)
    saved = load_json(PRIMARY/'cv_metrics.json')['logistic_regression']
    require(np.isclose(primary_cv['distinct_group']['mean_roc_auc'],saved['mean_roc_auc']), 'Saved primary CV mismatch')
    require({r['group_id'] for r in read_csv(PRIMARY/'test_predictions.csv')} == set(metrics['test_group_ids']), 'Holdouts differ')
    differences = {}
    for view in ['distinct_group','original_row_weighted']:
        differences[view] = {k:{'primary':primary[view][k],'repetition_weighted':metrics[view][k],
                                'signed_difference':metrics[view][k]-primary[view][k],
                                'absolute_difference':abs(metrics[view][k]-primary[view][k])}
                             for k in ['roc_auc','sensitivity','specificity','precision','f1','accuracy']}
    dump(OUT/'repetition_weighted_comparison.json',{'primary_cv_derived_from_saved_predictions':derived,
        'primary_cv_summary':primary_cv,'repetition_weighted_cv_summary':cv['summary'],
        'test_differences':differences,'same_test_groups':True})
    lines = ['# CardioLens AI Experiment 2: repetition-weighted training', '',
        '**Secondary exploratory evaluation on a previously inspected holdout.** These experiments share the same 61 test feature groups and are not independent evaluations.', '',
        'Only training-row inclusion changes: Experiment 1 fits one representative per group; Experiment 2 fits every original eligible row once. Both use the saved split and five folds, seed 42, fixed logistic regression (L2, C=1), identical preprocessing choices, and threshold 0.5. No model selection or tuning occurs in Experiment 2.', '',
        '## Training counts', '', '| Stage | Groups (both) | Experiment 1 training rows | Experiment 2 training rows | Validation groups / original rows |', '|---|---:|---:|---:|---|']
    for f in cv['folds']:
        lines.append(f"| Fold {f['fold']} | {f['training']['groups']} | {f['training']['groups']} | {f['training']['original_rows']} | {f['validation']['groups']} / {f['validation']['original_rows']} |")
    lines += ['| Final development fit | 241 | 241 | 811 | Test: 61 / 214 |', '',
        'Development class counts: 110 label-0 / 131 label-1 groups; 395 label-0 / 416 label-1 original rows. Test: 28 label-0 / 33 label-1 groups; 104 label-0 / 110 label-1 rows. Full per-fold counts are saved in the CV metrics.', '',
        '## Development cross-validation', '',
        '| View | Exp. 1 mean AUC | Exp. 1 fold SD | Exp. 2 mean AUC | Exp. 2 fold SD | Signed mean difference | Absolute mean difference | Absolute SD difference |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for view in primary_cv:
        a,b = primary_cv[view],cv['summary'][view]
        d=b['mean_roc_auc']-a['mean_roc_auc']
        lines.append(f"| {view} | {a['mean_roc_auc']:.6f} | {a['sample_sd_roc_auc']:.6f} | {b['mean_roc_auc']:.6f} | {b['sample_sd_roc_auc']:.6f} | {d:+.6f} | {abs(d):.6f} | {abs(b['sample_sd_roc_auc']-a['sample_sd_roc_auc']):.6f} |")
    lines += ['', 'Means are unweighted means of five fold AUCs; SD is sample SD (ddof=1), not a confidence interval. Experiment 1 row-weighted CV metrics were reconstructed from its saved logistic-regression out-of-fold predictions and original multiplicities; the primary model was not rerun or modified.', '',
        '## Shared final holdout', '', '| View | Metric | Experiment 1 | Experiment 2 | Signed difference (2 minus 1) | Absolute difference |', '|---|---|---:|---:|---:|---:|']
    for view, diffs in differences.items():
        for k,d in diffs.items():
            lines.append(f"| {view} | {k} | {d['primary']:.6f} | {d['repetition_weighted']:.6f} | {d['signed_difference']:+.6f} | {d['absolute_difference']:.6f} |")
    for view in differences:
        lines += ['',f"**{view}:** Experiment 1 confusion matrix `{primary[view]['confusion_matrix']}`; Experiment 2 `{metrics[view]['confusion_matrix']}`. Rows=true [0,1], columns=predicted [0,1].",
                  f"Experiment 2 metric denominators: `{metrics[view]['denominators']}`."]
    lines += ['', '## Interpretation and limits', '',
        'The comparison measures how observed repetition frequencies affect this pipeline on this split. The expanded data changes the numeric scaler statistics and the contribution of records to logistic-regression fitting. With C held fixed, changing total training sample count can also change the balance of data loss and regularization; this is not solely a comparison of relative group weights.', '',
        'A higher score would not establish a superior model; a lower score would not establish erroneous repetitions. No statistical-significance claim is made. Repeated rows are neither independent patients nor independent evidence. Small, previously inspected test data and unknown data generation limit interpretation. No test result was used to revise the experiment.', '',
        'Dataset provenance, feature definitions/category codes, and target=1 semantics remain unverified. Sensitivity is recall of numeric label 1. Groups represent identical features, not patient identities. The comparison establishes no patient-level independence, clinical validity, diagnostic accuracy, or generalization to new patients.', '',
        'Encoding assumptions are inherited: age, trestbps, chol, thalach, oldpeak standardized; sex, cp, fbs, restecg, exang, slope, ca, thal one-hot encoded as nominal categories with unknown categories ignored. ca=4 and thal=0 remain unchanged. The scaler learns from expanded training rows; the encoder learns only categories present in those rows. No imputation or label alteration.', '',
        '## Verification and reproduction', '',
        'The runner checks source/primary hashes before and after execution and logs every fitting source-row number, group, multiplicity, scaler statistics, and category set. The separate verification script independently checks predictions, metric denominators, confusion matrices, pairwise AUCs, and training membership. Its authoritative result is repetition_weighted_verification.json.', '',
        'From the workspace root, using the primary pinned environment:', '', '```powershell',
        '& work/baseline-env/Scripts/python.exe -B outputs/repetition_weighted/run_repetition_weighted.py',
        '& work/baseline-env/Scripts/python.exe -B outputs/repetition_weighted/verify_repetition_weighted.py', '```', '',
        'Configuration contains the inherited settings and pre-experiment hashes of all primary files. Primary helpers are imported read-only with bytecode writes disabled. Environment and script hashes are saved. Rerunning reproduces the same exploratory evaluation; it is not a fresh holdout. No UI is created.']
    (OUT/'repetition_weighted_comparison.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def main():
    config_path = OUT/'repetition_weighted_config.json'
    design = load_json(config_path)
    frozen_hash = sha(config_path)
    cfg, rows, groups = inputs(design)
    dev = {g for g,r in groups.items() if r['partition']=='development'}
    test = {g for g,r in groups.items() if r['partition']=='test'}
    require(len(dev)==241 and len(test)==61 and not dev & test, 'Saved partitions invalid')
    events = [{'phase':'design_frozen','config_sha256':frozen_hash,'model':'logistic_regression',
               'model_selection':False,'threshold':cfg['threshold'],'test_previously_inspected':True}]
    fold_metrics, cv_predictions, cv_rows = [], [], []
    # Training routine only receives development rows, never test rows or labels.
    dev_rows = [r for r in rows if r['group_id'] in dev]
    for fold in range(1,cfg['cv_folds']+1):
        valid = {g for g in dev if int(groups[g]['validation_fold'])==fold}
        train = dev-valid
        train_rows = [r for r in dev_rows if r['group_id'] in train]
        require(len(train_rows)==sum(int(groups[g]['original_row_count']) for g in train), 'Missing training copies')
        model = fit_expanded(train_rows,train,valid|test,cfg,f'cv_fit_{fold}',events)
        predictions = predict_groups(model,valid,groups,cfg,fold,events)
        expanded = expand_predictions(predictions,dev_rows)
        fold_metrics.append({'fold':fold,'training_group_ids':sorted(train),'validation_group_ids':sorted(valid),
            'training':count_groups(train,rows,groups),'validation':count_groups(valid,rows,groups),
            'distinct_group':evaluate(predictions),'original_row_weighted':evaluate(expanded)})
        cv_predictions.extend(predictions); cv_rows.extend(expanded)
    cv={'folds':fold_metrics,'summary':summary(fold_metrics)}
    dump(OUT/'repetition_weighted_cv_metrics.json',cv)
    write_csv(OUT/'repetition_weighted_cv_predictions.csv',cv_predictions)
    write_csv(OUT/'repetition_weighted_cv_row_predictions.csv',cv_rows)
    require(sha(config_path)==frozen_hash,'Design changed during CV')
    events.append({'phase':'cv_complete','model_selection':False,'config_sha256':frozen_hash})
    final=fit_expanded(dev_rows,dev,test,cfg,'final_development_fit',events)
    predictions=predict_groups(final,test,groups,cfg,0,events)
    expanded=expand_predictions(predictions,rows)
    metrics={'experiment':'repetition_weighted_training','model':'logistic_regression',
        'test_group_ids':sorted(test),'counts':{'development':count_groups(dev,rows,groups),'test':count_groups(test,rows,groups)},
        'distinct_group':evaluate(predictions),'original_row_weighted':evaluate(expanded),
        'threshold':cfg['threshold'],'positive_class':'numeric target=1; semantics unverified',
        'secondary_exploratory_shared_holdout':True}
    for view in ['distinct_group','original_row_weighted']:
        metrics[view].update({'group_count':len(test),'represented_original_rows':len(expanded)})
    write_csv(OUT/'repetition_weighted_test_predictions.csv',predictions)
    write_csv(OUT/'repetition_weighted_test_row_predictions.csv',expanded)
    dump(OUT/'repetition_weighted_metrics.json',metrics)
    joblib.dump(final,OUT/'repetition_weighted_model.joblib')
    comparison(metrics,cv,rows,groups)
    check_frozen(design)
    require(sha(config_path)==frozen_hash,'Design changed after test')
    events.append({'phase':'integrity_verified','source_sha256':sha(Path(cfg['source_path'])),
                   'primary_files_unchanged':len(design['primary_file_sha256']),'config_sha256':frozen_hash})
    dump(OUT/'repetition_weighted_execution.json',events)
    dump(OUT/'repetition_weighted_environment.json',{'python':platform.python_version(),
        'numpy':np.__version__,'scipy':scipy.__version__,'scikit-learn':sklearn.__version__,
        'joblib':joblib.__version__,'threadpoolctl':threadpoolctl.__version__,
        'runner_sha256':sha(Path(__file__)),'config_sha256':frozen_hash,
        'primary_helpers_sha256':sha(PRIMARY/'run_baseline.py'),'executable':sys.executable})
    dump(OUT/'repetition_weighted_run_status.json',{'status':'PASS','errors':[],
        'source_unchanged':True,'primary_files_unchanged':True,'convergence_errors':0})
    print(json.dumps({'status':'PASS','cv_summary':cv['summary'],'test':metrics},indent=2))


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        dump(OUT/'repetition_weighted_run_status.json',{'status':'FAIL','errors':[f'{type(exc).__name__}: {exc}']})
        raise
