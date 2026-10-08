"""CardioLens educational baseline. Run with Python 3.12 and pinned requirements.
python outputs/run_baseline.py --config outputs/baseline_config.json
Source is opened read-only. All generated files go beside the configuration.
"""
import argparse
import csv
import hashlib
import io
import json
import platform
import sys
import warnings
from collections import Counter
from decimal import Decimal
from pathlib import Path

import joblib
import numpy as np
import scipy
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def ratio(a, b):
    return float(a / b) if b else None


def score(y, prediction, probability):
    tn, fp, fn, tp = [int(v) for v in confusion_matrix(y, prediction, labels=[0, 1]).ravel()]
    return {'n': len(y), 'class_counts': {'0': int(sum(y == 0)), '1': int(sum(y == 1))},
            'confusion_matrix': [[tn, fp], [fn, tp]],
            'confusion_matrix_order': 'rows=true [0,1], columns=predicted [0,1]',
            'sensitivity': ratio(tp, tp + fn), 'specificity': ratio(tn, tn + fp),
            'precision': ratio(tp, tp + fp), 'f1': ratio(2 * tp, 2 * tp + fp + fn),
            'accuracy': ratio(tp + tn, len(y)),
            'roc_auc': float(roc_auc_score(y, probability)) if len(set(y)) == 2 else None,
            'denominators': {'sensitivity': tp + fn, 'specificity': tn + fp,
                'precision': tp + fp, 'f1': 2 * tp + fp + fn, 'accuracy': len(y),
                'roc_auc_positive_negative_pairs': (tp + fn) * (tn + fp)},
            'undefined_policy': 'null if denominator is zero; ROC-AUC null if either label is absent'}


def counts(ids, group_map):
    selected = [group_map[g] for g in ids]
    return {'groups': len(selected), 'original_rows': sum(g['multiplicity'] for g in selected),
            'group_class_counts': {str(c): sum(g['target'] == c for g in selected) for c in (0, 1)},
            'row_class_counts': {str(c): sum(g['multiplicity'] for g in selected if g['target'] == c) for c in (0, 1)}}


def make_model(name, cfg):
    if name == 'majority':
        return Pipeline([('model', DummyClassifier(strategy='most_frequent'))])
    require(name == 'logistic_regression', 'Unknown candidate')
    num = [cfg['features'].index(c) for c in cfg['numeric_features']]
    cat = [cfg['features'].index(c) for c in cfg['categorical_features']]
    preprocess = ColumnTransformer([
        ('numeric', StandardScaler(), num),
        ('categorical', OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop=None), cat)
    ], remainder='drop')
    return Pipeline([('preprocess', preprocess),
                     ('model', LogisticRegression(random_state=cfg['seed'], **cfg['logistic_regression']))])


def fit_checked(name, cfg, X, y, ids, allowed_ids, test_ids, events, phase):
    require(len(ids) == len(set(ids)) == len(X), 'Training must use exactly one row per feature group')
    require(set(ids) <= set(allowed_ids) and not set(ids) & set(test_ids), 'Forbidden group in fit')
    model = make_model(name, cfg)
    with warnings.catch_warnings():
        warnings.simplefilter('error', ConvergenceWarning)
        model.fit(X, y)
    fitted = {'phase': phase, 'candidate': name, 'fit_group_ids': list(ids),
              'training_rows': len(X), 'one_row_per_group': True, 'test_overlap': 0}
    if name == 'logistic_regression':
        prep = model.named_steps['preprocess']
        nums = [cfg['features'].index(c) for c in cfg['numeric_features']]
        cats = [cfg['features'].index(c) for c in cfg['categorical_features']]
        scaler = prep.named_transformers_['numeric']
        encoder = prep.named_transformers_['categorical']
        require(np.allclose(scaler.mean_, X[:, nums].mean(axis=0)), 'Scaler used unexpected data')
        require(int(scaler.n_samples_seen_) == len(ids), 'Wrong scaler sample count')
        require(all(np.array_equal(values, np.unique(X[:, column]))
                    for values, column in zip(encoder.categories_, cats)), 'Encoder used unexpected categories')
        fitted.update({'scaler_training_count': int(scaler.n_samples_seen_),
                       'scaler_mean': scaler.mean_.tolist(),
                       'learned_categories': {name: values.tolist() for name, values in zip(cfg['categorical_features'], encoder.categories_)},
                       'iterations': model.named_steps['model'].n_iter_.tolist(),
                       'training_only_preprocessing_verified': True})
    events.append(fitted)
    return model


def predict(model, X, cfg):
    probability = model.predict_proba(X)[:, list(model.classes_).index(1)]
    return (probability >= cfg['threshold']).astype(int), probability


def select_on_development(X, y, ids, folds, cfg, test_ids, events):
    """Receives development features/labels only; test_ids are a forbidden-ID guard."""
    require(not set(ids) & set(test_ids), 'Test IDs passed into model selection')
    summaries, predictions = {}, []
    for name in cfg['candidate_order']:
        results = []
        for fold in range(1, cfg['cv_folds'] + 1):
            train = np.flatnonzero(folds != fold)
            valid = np.flatnonzero(folds == fold)
            require(not set(ids[train]) & set(ids[valid]), 'Train/validation feature overlap')
            model = fit_checked(name, cfg, X[train], y[train], ids[train], ids, test_ids, events, f'cv_{fold}')
            pred, prob = predict(model, X[valid], cfg)
            results.append({'fold': fold, 'train_groups': len(train), 'validation_groups': len(valid),
                            'validation_group_ids': ids[valid].tolist(), 'metrics': score(y[valid], pred, prob)})
            predictions.extend({'candidate': name, 'fold': fold, 'group_id': str(ids[i]),
                                'target': int(y[i]), 'prediction': int(p), 'probability_target_1': float(q)}
                               for i, p, q in zip(valid, pred, prob))
        aucs = [r['metrics']['roc_auc'] for r in results]
        require(all(a is not None for a in aucs), 'ROC-AUC unavailable for model selection')
        summaries[name] = {'folds': results, 'mean_roc_auc': float(np.mean(aucs)),
                           'sample_sd_roc_auc': float(np.std(aucs, ddof=1))}
    winner = max(cfg['candidate_order'], key=lambda name: summaries[name]['mean_roc_auc'])
    return winner, summaries, predictions


def main(config_path):
    config_path = config_path.resolve()
    out = config_path.parent
    cfg = json.loads(config_path.read_text(encoding='utf-8'))
    source = Path(cfg['source_path']).resolve(strict=True)
    # Guard every output name against accidental source aliasing.
    names = ['group_manifest.csv', 'group_split.csv', 'cv_metrics.json', 'cv_predictions.csv',
             'model_selection.json', 'test_predictions.csv', 'test_row_predictions.csv',
             'baseline_metrics.json', 'baseline_checks.json', 'baseline_report.md',
             'baseline_execution.json', 'baseline_environment.json', 'baseline_model.joblib']
    for name in names:
        target = out / name
        require(target.resolve() != source and not (target.exists() and target.samefile(source)), 'Output aliases source')
    before = digest(source.read_bytes())
    require(before == cfg['source_sha256'], 'Source differs from approved audit; stopping')
    require(sorted(cfg['numeric_features'] + cfg['categorical_features']) == sorted(cfg['features']), 'Feature roles must partition features')
    reader = csv.reader(io.StringIO(source.read_bytes().decode('utf-8-sig'), newline=''), strict=True)
    headers = next(reader)
    require(headers == cfg['features'] + ['target'], 'Unexpected schema')
    groups, original, previous_line = {}, [], reader.line_num
    numeric_keys = {}
    for ordinal, row in enumerate(reader, 1):
        require(len(row) == 14 and row[-1] in ('0', '1'), 'Malformed data or target')
        feature_key = tuple(row[:-1])
        normalized = tuple(Decimal(v) for v in feature_key)
        require(all(v.is_finite() for v in normalized), 'Nonfinite feature')
        gid = digest(json.dumps([cfg['features'], list(feature_key)], separators=(',', ':')).encode('utf-8'))
        if normalized in numeric_keys:
            require(numeric_keys[normalized] == gid, 'Raw and numeric feature grouping differ; review required')
        numeric_keys[normalized] = gid
        if gid not in groups:
            groups[gid] = {'key': feature_key, 'target': int(row[-1]), 'multiplicity': 0,
                           'representative_record': ordinal, 'representative_line_start': previous_line + 1}
        require(groups[gid]['key'] == feature_key, 'Hash collision')
        require(groups[gid]['target'] == int(row[-1]), 'Conflicting group labels; stopping')
        groups[gid]['multiplicity'] += 1
        original.append({'record_number': ordinal, 'csv_line_start': previous_line + 1,
                         'csv_line_end': reader.line_num, 'group_id': gid, 'target': int(row[-1])})
        previous_line = reader.line_num
    require(len(original) == cfg['expected_rows'] and len(groups) == cfg['expected_groups'], 'Unexpected counts')
    # Sort by content ID: split ordering is explicit and independent of source row order.
    ids = np.array(sorted(groups))
    y = np.array([groups[g]['target'] for g in ids])
    dev, test = train_test_split(ids, test_size=cfg['test_fraction'], stratify=y, random_state=cfg['seed'])
    dev, test = np.sort(dev), np.sort(test)
    require(not set(dev) & set(test), 'Development/test overlap')
    require(set(dev) | set(test) == set(ids), 'Incomplete split')
    dev_y = np.array([groups[g]['target'] for g in dev])
    folds = np.zeros(len(dev), dtype=int)
    skf = StratifiedKFold(n_splits=cfg['cv_folds'], shuffle=True, random_state=cfg['seed'])
    for fold, (train, valid) in enumerate(skf.split(dev, dev_y), 1):
        require(not set(dev[train]) & set(dev[valid]) and not (set(dev[train]) | set(dev[valid])) & set(test), 'Fold overlap')
        folds[valid] = fold
    fold_lookup = {str(g): int(f) for g, f in zip(dev, folds)}
    partition = {str(g): 'development' for g in dev} | {str(g): 'test' for g in test}
    split_rows = [{'group_id': str(g), 'partition': partition[g], 'validation_fold': fold_lookup.get(g, ''),
                   'target': groups[g]['target'], 'original_row_count': groups[g]['multiplicity'],
                   'representative_record': groups[g]['representative_record'],
                   'representative_line_start': groups[g]['representative_line_start'],
                   'seed': cfg['seed'], **dict(zip(cfg['features'], groups[g]['key']))} for g in ids]
    manifest = [{**r, 'partition': partition[r['group_id']], 'validation_fold': fold_lookup.get(r['group_id'], ''),
                 'group_row_count': groups[r['group_id']]['multiplicity'],
                 'is_representative': r['record_number'] == groups[r['group_id']]['representative_record']} for r in original]
    # Existing split must match exactly; reruns cannot silently replace split assignments.
    if (out / 'group_split.csv').exists():
        with (out / 'group_split.csv').open(newline='', encoding='utf-8') as f:
            saved = list(csv.DictReader(f))
        require(saved == [{k: str(v) for k, v in r.items()} for r in split_rows], 'Existing split differs; use separate experiment folder')
    write_csv(out / 'group_split.csv', split_rows)
    write_csv(out / 'group_manifest.csv', manifest)
    events = []
    dev_X = np.array([groups[g]['key'] for g in dev], dtype=float)
    winner, cv, cv_predictions = select_on_development(dev_X, dev_y, dev, folds, cfg, test, events)
    dump(out / 'cv_metrics.json', cv)
    write_csv(out / 'cv_predictions.csv', cv_predictions)
    selection = {'selected_model': winner, 'selection_metric': cfg['selection_metric'],
                 'development_mean_roc_auc': {k: v['mean_roc_auc'] for k, v in cv.items()},
                 'tie_break': cfg['tie_break'], 'threshold_fixed_before_evaluation': cfg['threshold'],
                 'selection_group_ids': dev.tolist(), 'test_group_overlap': 0,
                 'test_features_or_labels_passed_to_selector': False,
                 'test_labels_used_for_initial_stratification_only': True,
                 'config_sha256': digest(config_path.read_bytes()),
                 'split_sha256': digest((out / 'group_split.csv').read_bytes())}
    # Persist/freeze selection BEFORE any test prediction or test scoring.
    dump(out / 'model_selection.json', selection)
    selection_hash = digest((out / 'model_selection.json').read_bytes())
    events.append({'phase': 'selection_frozen', 'sha256': selection_hash, 'selected_model': winner})
    final = fit_checked(winner, cfg, dev_X, dev_y, dev, dev, test, events, 'final_development_fit')
    test_X = np.array([groups[g]['key'] for g in test], dtype=float)
    test_y = np.array([groups[g]['target'] for g in test])
    pred, prob = predict(final, test_X, cfg)
    events.append({'phase': 'final_test_prediction', 'group_ids': test.tolist(), 'selected_model': winner})
    group_predictions = [{'group_id': str(g), 'target': int(t), 'prediction': int(p),
                          'probability_target_1': float(q), 'original_row_count': groups[g]['multiplicity']}
                         for g, t, p, q in zip(test, test_y, pred, prob)]
    by_group = {r['group_id']: r for r in group_predictions}
    row_predictions = [{**r, 'prediction': by_group[r['group_id']]['prediction'],
                        'probability_target_1': by_group[r['group_id']]['probability_target_1']}
                       for r in original if r['group_id'] in by_group]
    metrics = {'experiment': 'primary_one_row_per_training_group', 'selected_model': winner,
        'positive_class': 'numeric target=1; clinical semantics unverified',
        'counts': {'all': counts(ids, groups), 'development': counts(dev, groups), 'test': counts(test, groups),
                   'cv': [{'fold': f, 'training': counts(dev[folds != f], groups),
                           'validation': counts(dev[folds == f], groups)} for f in range(1, cfg['cv_folds'] + 1)]},
        'distinct_group': score(test_y, pred, prob),
        'original_row_weighted': score(np.array([r['target'] for r in row_predictions]),
            np.array([r['prediction'] for r in row_predictions]), np.array([r['probability_target_1'] for r in row_predictions]))}
    metrics['distinct_group'].update({'group_count': len(test), 'represented_original_rows': len(row_predictions)})
    metrics['original_row_weighted'].update({'group_count': len(test), 'original_row_count': len(row_predictions)})
    require(digest((out / 'model_selection.json').read_bytes()) == selection_hash, 'Selection changed after test evaluation')
    require(all(not set(e.get('fit_group_ids', [])) & set(test) for e in events), 'Test used in fit')
    require(all(Counter(r['group_id'] for r in cv_predictions if r['candidate'] == name) == Counter(dev.tolist())
                for name in cfg['candidate_order']), 'Each development group must validate exactly once per candidate')
    after = digest(source.read_bytes())
    require(before == after, 'Source changed during execution')
    checks = {'status': 'PASS', 'source_sha256_before': before, 'source_sha256_after': after,
        'source_unchanged': before == after, 'manifest_covers_every_source_record_once': len(manifest) == len(original) == len({r['record_number'] for r in manifest}),
        'consistent_label_per_group': True, 'numeric_and_raw_groupings_agree': True,
        'development_test_group_overlap': len(set(dev) & set(test)),
        'cv_pairwise_train_validation_test_overlap': [0] * cfg['cv_folds'],
        'each_development_group_validates_once_per_candidate': True,
        'training_one_row_per_group': True, 'preprocessing_training_only_checked': True,
        'test_excluded_from_selection_and_fitting': True, 'selection_frozen_before_test_prediction': True,
        'selection_sha256': selection_hash, 'final_test_prediction_calls': 1,
        'scope': 'Runtime guards and saved fit/selection IDs verify this execution. Initial target-stratified allocation necessarily uses labels; no test score guides selection.',
        'errors': []}
    write_csv(out / 'test_predictions.csv', group_predictions)
    write_csv(out / 'test_row_predictions.csv', row_predictions)
    dump(out / 'baseline_metrics.json', metrics)
    dump(out / 'baseline_checks.json', checks)
    dump(out / 'baseline_execution.json', events)
    dump(out / 'baseline_environment.json', {'python': platform.python_version(), 'numpy': np.__version__,
        'scipy': scipy.__version__, 'scikit-learn': sklearn.__version__, 'joblib': joblib.__version__,
        'script_sha256': digest(Path(__file__).read_bytes()), 'config_sha256': digest(config_path.read_bytes()),
        'executable': sys.executable, 'argv': sys.argv})
    joblib.dump(final, out / 'baseline_model.joblib')
    report = ['# CardioLens AI baseline', '', 'Primary experiment: one representative per training feature group. Original CSV and every source-row mapping are preserved.', '',
        '## Results', '', f"Selected **{winner}** by development-only mean five-fold ROC-AUC; seed {cfg['seed']}, fixed threshold {cfg['threshold']}. No hyperparameter or threshold search.", '',
        '| Candidate | Mean development ROC-AUC | Fold sample SD |', '|---|---:|---:|']
    for name, result in cv.items():
        report.append(f"| {name} | {result['mean_roc_auc']:.6f} | {result['sample_sd_roc_auc']:.6f} |")
    report += ['', 'Only the selected model is scored on the final test. Fold SD is descriptive, not a confidence interval.', '',
        '| Partition | Groups | Original rows | Group labels 0 / 1 | Row labels 0 / 1 |', '|---|---:|---:|---|---|']
    for name in ['all', 'development', 'test']:
        c = metrics['counts'][name]
        report.append(f"| {name} | {c['groups']} | {c['original_rows']} | {c['group_class_counts']['0']} / {c['group_class_counts']['1']} | {c['row_class_counts']['0']} / {c['row_class_counts']['1']} |")
    report += ['', 'The requested 80/20 group split rounds to 241 development and 61 test groups. Row proportions differ because group multiplicities differ.', '',
        '| Test view | N | Sensitivity | Specificity | Precision | F1 | ROC-AUC |', '|---|---:|---:|---:|---:|---:|---:|']
    for name in ['distinct_group', 'original_row_weighted']:
        m = metrics[name]
        report.append('| ' + name + ' | ' + str(m['n']) + ' | ' + ' | '.join('undefined' if m[k] is None else f'{m[k]:.6f}' for k in ['sensitivity','specificity','precision','f1','roc_auc']) + ' |')
    for name in ['distinct_group', 'original_row_weighted']:
        report += ['', f"**{name} confusion matrix:** `{metrics[name]['confusion_matrix']}`; rows=true 0/1, columns=predicted 0/1.",
                   f"Metric denominators: `{metrics[name]['denominators']}`."]
    report += ['', 'The row-weighted view expands the same held-out group predictions back to their source rows; it does not retrain. These are test-subset results, not out-of-sample scores for all 1,025 rows. Repeated rows do not supply independent evidence.', '',
        '## Methods and assumptions', '', cfg['encoding_assumptions'], '',
        'Group IDs hash ordered raw feature strings, excluding target. Numeric-normalized grouping was checked to agree. Representatives are first source occurrences; grouping collapses only the modeling view, never the CSV. CSV lines are physical, 1-based including the header; record numbers are logical data records after the header.', '',
        'Groups sorted by ID are stratified 80/20 using seed 42. Development groups receive five fixed stratified folds. A fresh pipeline is fit for each candidate/fold. The majority classifier predicts the training majority; logistic regression uses L2 regularization with C=1. Categories and numeric scaling are learned inside each fit. Unseen category codes produce all-zero one-hot blocks. No imputation or category correction is performed.', '',
        'The selection function receives only development features and labels. Test group IDs serve solely as an exclusion guard. Test labels are used for the initial requested stratification and final scoring, not model selection. The saved selection is hashed before test prediction and verified unchanged afterward. All fits record their group IDs in baseline_execution.json.', '',
        '## Checks and limitations', '',
        'All baseline runtime checks passed: complete row coverage; consistent group labels; zero train/validation/test overlap within each fold; no test group in selection or fits; one representative per training group; training-only scaler/category checks; one final test prediction call; unchanged source hash.', '',
        f'Source SHA-256 before and after: `{before}`.', '',
        'Dataset provenance, feature definitions/category codes, and target=1 semantics remain unverified. Sensitivity here means recall of numeric label 1; it is not established disease sensitivity. Feature groups are not patient identifiers. This educational experiment does not establish patient-level separation, clinical validity, diagnostic accuracy, or generalization to real patients. The small test set and unknown dependence limit conclusions; row weighting changes the estimand, not evidence strength. Test results must not drive further tuning on this same holdout.', '',
        'Project context: MILF_Problem_Statements_Reference_Style (1).pdf p. 2, Problem Statement 3 describes the educational objective and metrics but supplies no verified codebook. Lightweight ML Primer for Freshers.pdf pp. 9-12 and 28-29 gives generic preprocessing/evaluation guidance; p. 39 describes the heart challenge. Neither resolves provenance or repetition.', '',
        'Optional repetition-weighted training was not run. No UI was built.', '',
        '## Reproduce', '', 'Use Python 3.12 and the exact dependency versions in baseline_requirements.txt. From the workspace root:', '',
        '```powershell', 'py -3.12 -m venv work/baseline-env', '& work/baseline-env/Scripts/python.exe -m pip install -r outputs/baseline_requirements.txt',
        '& work/baseline-env/Scripts/python.exe outputs/run_baseline.py --config outputs/baseline_config.json', '```', '',
        'The source hash must match the approved audit; mismatches stop the run. Existing split assignments must match exactly. A rerun is reproduction, not a new independent test. Configuration, split, script hashes, versions, predictions, and metric denominators are saved. The serialized pipeline is baseline_model.joblib; load only trusted local model files.', '',
        'Implementation references: [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html), [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).']
    (out / 'baseline_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'selected_model': winner, 'cv_auc': selection['development_mean_roc_auc'],
                      'test_groups': len(test), 'test_rows': len(row_predictions),
                      'test_distinct': metrics['distinct_group'], 'test_row_weighted': metrics['original_row_weighted'],
                      'source_unchanged': True}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path(__file__).with_name('baseline_config.json'))
    args = parser.parse_args()
    try:
        main(args.config)
    except Exception as exc:
        print(f'FAILED: {type(exc).__name__}: {exc}', file=sys.stderr)
        raise
