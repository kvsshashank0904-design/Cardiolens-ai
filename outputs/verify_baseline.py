"""Independently verify saved artifacts without retraining or creating a new split file."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.model_selection import StratifiedKFold, train_test_split


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def read_csv(path):
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def main():
    out = Path(__file__).resolve().parent
    load = lambda name: json.loads((out / name).read_text(encoding='utf-8'))
    cfg, metrics, checks = load('baseline_config.json'), load('baseline_metrics.json'), load('baseline_checks.json')
    source = Path(cfg['source_path'])
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    require(source_hash == cfg['source_sha256'] == checks['source_sha256_before'] == checks['source_sha256_after'], 'Source integrity')
    raw, manifest, splits = read_csv(source), read_csv(out/'group_manifest.csv'), read_csv(out/'group_split.csv')
    require(len(raw) == len(manifest) == 1025 and len(splits) == 302, 'Record coverage')
    require([int(r['record_number']) for r in manifest] == list(range(1, 1026)), 'Source row mapping')
    split_map = {r['group_id']: r for r in splits}
    grouped = defaultdict(list)
    for ordinal, (record, mapping) in enumerate(zip(raw, manifest), 1):
        key = [cfg['features'], [record[f] for f in cfg['features']]]
        gid = hashlib.sha256(json.dumps(key, separators=(',', ':')).encode()).hexdigest()
        require(mapping['group_id'] == gid, 'Feature-only group ID')
        require(mapping['target'] == record['target'] == split_map[gid]['target'], 'Label preservation/consistency')
        require(int(mapping['csv_line_start']) == int(mapping['csv_line_end']) == ordinal + 1, 'Physical CSV line reference')
        require(mapping['partition'] == split_map[gid]['partition'] and mapping['validation_fold'] == split_map[gid]['validation_fold'], 'Entire group assigned consistently')
        require(all(split_map[gid][f] == record[f] for f in cfg['features']), 'Representative features')
        grouped[gid].append(mapping)
    for gid, rows in grouped.items():
        require(len(rows) == int(split_map[gid]['original_row_count']), 'Multiplicity')
        require(sum(r['is_representative'] == 'True' for r in rows) == 1, 'Exactly one representative')
        require(int(split_map[gid]['representative_record']) == min(int(r['record_number']) for r in rows), 'First occurrence representative')
    ids = np.array(sorted(grouped))
    labels = np.array([int(split_map[g]['target']) for g in ids])
    replay_dev, replay_test = train_test_split(ids, test_size=cfg['test_fraction'], stratify=labels, random_state=cfg['seed'])
    dev = {r['group_id'] for r in splits if r['partition'] == 'development'}
    test = set(ids) - dev
    require(dev == set(replay_dev) and test == set(replay_test), 'Seeded split reproducibility')
    require(len(dev) == 241 and len(test) == 61 and not dev & test, 'Development/test separation')
    ordered_dev = np.array(sorted(dev))
    folds = StratifiedKFold(n_splits=cfg['cv_folds'], shuffle=True, random_state=cfg['seed'])
    for fold, (_, valid) in enumerate(folds.split(ordered_dev, [int(split_map[g]['target']) for g in ordered_dev]), 1):
        require(all(int(split_map[g]['validation_fold']) == fold for g in ordered_dev[valid]), 'Fold reproducibility')
    cv, selection, events = load('cv_metrics.json'), load('model_selection.json'), load('baseline_execution.json')
    require(set(selection['selection_group_ids']) == dev and not set(selection['selection_group_ids']) & test, 'Selection excludes test')
    aucs = {name: np.mean([f['metrics']['roc_auc'] for f in value['folds']]) for name, value in cv.items()}
    winner = max(cfg['candidate_order'], key=lambda name: aucs[name])
    require(winner == selection['selected_model'] == metrics['selected_model'], 'Development-only selection rule')
    require(selection['config_sha256'] == hashlib.sha256((out/'baseline_config.json').read_bytes()).hexdigest(), 'Config hash')
    require(selection['split_sha256'] == hashlib.sha256((out/'group_split.csv').read_bytes()).hexdigest(), 'Split hash')
    phases = [e['phase'] for e in events]
    require(phases.count('selection_frozen') == phases.count('final_test_prediction') == 1, 'Single freeze and test call')
    require(phases.index('selection_frozen') < phases.index('final_development_fit') < phases.index('final_test_prediction'), 'Selection precedes test')
    require(checks['selection_sha256'] == hashlib.sha256((out/'model_selection.json').read_bytes()).hexdigest(), 'Selection remained frozen')
    require(sum('fit_group_ids' in e for e in events) == 11, 'Ten CV fits and one final fit')
    for e in events:
        if 'fit_group_ids' not in e:
            continue
        fitted = set(e['fit_group_ids'])
        require(len(fitted) == len(e['fit_group_ids']) == e['training_rows'], 'No repeated training groups')
        require(not fitted & test, 'Test excluded from all fits')
        if e['phase'].startswith('cv_'):
            fold = int(e['phase'].split('_')[1])
            valid = {g for g in dev if int(split_map[g]['validation_fold']) == fold}
            require(fitted == dev - valid and not fitted & valid, 'CV exact train/validation membership')
        else:
            require(fitted == dev, 'Final fit uses all and only development')
        if e['candidate'] == 'logistic_regression':
            x = np.array([[float(split_map[g][f]) for f in cfg['numeric_features']] for g in e['fit_group_ids']])
            require(np.allclose(x.mean(axis=0), e['scaler_mean']), 'Training-only scaler means')
            for f in cfg['categorical_features']:
                require(sorted({float(split_map[g][f]) for g in fitted}) == e['learned_categories'][f], 'Training-only encoder categories')
    cv_predictions = read_csv(out/'cv_predictions.csv')
    for name in cfg['candidate_order']:
        rows = [r for r in cv_predictions if r['candidate'] == name]
        require(Counter(r['group_id'] for r in rows) == Counter(dev), 'Each development group predicted once per candidate')
        require(all(int(r['fold']) == int(split_map[r['group_id']]['validation_fold']) for r in rows), 'OOF membership')
    test_groups, test_rows = read_csv(out/'test_predictions.csv'), read_csv(out/'test_row_predictions.csv')
    require({r['group_id'] for r in test_groups} == test and len(test_groups) == 61, 'Final test group coverage')
    by_id = {r['group_id']: r for r in test_groups}
    require(Counter(int(r['record_number']) for r in test_rows) == Counter(int(r['record_number']) for r in manifest if r['partition'] == 'test'), 'Complete original-row test expansion')
    for r in test_rows:
        require(all(r[f] == by_id[r['group_id']][f] for f in ['target','prediction','probability_target_1']), 'Same group prediction expanded')
    for view, rows in [('distinct_group', test_groups), ('original_row_weighted', test_rows)]:
        m = metrics[view]
        cells = Counter((int(r['target']), int(r['prediction'])) for r in rows)
        matrix = [[cells[0,0], cells[0,1]], [cells[1,0], cells[1,1]]]
        require(matrix == m['confusion_matrix'] and len(rows) == m['n'], 'Confusion matrix/denominator recomputation')
        tn, fp, fn, tp = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        expected = {'sensitivity': tp/(tp+fn), 'specificity': tn/(tn+fp), 'precision': tp/(tp+fp),
                    'f1': 2*tp/(2*tp+fp+fn), 'accuracy': (tp+tn)/len(rows)}
        positives = [float(r['probability_target_1']) for r in rows if r['target'] == '1']
        negatives = [float(r['probability_target_1']) for r in rows if r['target'] == '0']
        expected['roc_auc'] = sum((p > n) + .5*(p == n) for p in positives for n in negatives)/(len(positives)*len(negatives))
        require(all(abs(m[k]-value) < 1e-12 for k,value in expected.items()), 'Independent metric recomputation')
    # Exercise the contamination guard without fitting any model.
    from run_baseline import fit_checked
    blocked = False
    try:
        fit_checked('majority', cfg, np.zeros((1,13)), np.array([0]), [next(iter(test))], dev, test, [], 'guard_test')
    except ValueError:
        blocked = True
    require(blocked, 'Contaminated fit must be rejected before training')
    result = {'status': 'PASS', 'source_unchanged': True,
              'verified': ['source-row and group-key reconstruction', 'all label and feature values preserved',
                'saved split and folds reproduce from seed', 'CV/final fit membership and one row per group',
                'training-only scaler/category trace', 'development-only selection and frozen decision hash',
                'complete test-row prediction expansion', 'independent confusion matrices, metrics and pairwise ROC-AUC',
                'intentional test-group contamination rejected before fit'],
              'errors': [], 'no_models_retrained': True}
    (out/'baseline_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
