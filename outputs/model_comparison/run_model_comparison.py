"""Experiment 4: fixed MLP, frozen Experiment 3 comparator. Never run prior mains."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
import platform
import warnings
from pathlib import Path
import joblib
import numpy as np
import scipy
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from threadpoolctl import threadpool_limits, threadpool_info

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(BASE / 'corrected_label_baseline'))
import run_corrected_label_baseline as e3

VIEWS = ['distinct_group', 'original_row_weighted']
MEASURES = ['sensitivity', 'specificity', 'precision', 'f1', 'accuracy', 'roc_auc']

def protect(config):
    e3.require(e3.sha(Path(config['source_path'])) == config['source_sha256'], 'Source changed')
    for name, digest in config['protected_sha256'].items():
        e3.require((BASE/name).is_file() and e3.sha(BASE/name) == digest, 'Protected changed: '+name)

def cv_summary(folds):
    return {v: {k: {'mean': float(np.mean([f[v][k] for f in folds])),
                          'sample_sd': float(np.std([f[v][k] for f in folds], ddof=1))}
                for k in MEASURES} for v in VIEWS}

def run(config, out):
    protect(config)
    design = e3.load(BASE/'corrected_label_baseline/corrected_label_config.json')
    cfg, groups, mapped, derived = e3.checked_inputs(design)
    frozen_manifest = e3.read_csv(BASE/'corrected_label_baseline/corrected_group_manifest.csv')
    for g in frozen_manifest:
        e3.require(int(g['disease_present']) == mapped[g['group_id']]['disease_present'], 'Corrected label differs')
    dev = {g for g,r in groups.items() if r['partition']=='development'}
    test = set(groups)-dev
    e3.require(len(dev)==241 and len(test)==61 and not dev & test, 'Split changed')
    config_hash = e3.sha(HERE/'model_comparison_config.json')
    events = [{'phase':'design_frozen', 'config_sha256':config_hash,
               'selection':'none; single prespecified configuration and threshold', 'test_used_for_selection':False}]
    e3.dump(out/'configuration.json', config)
    e3.write_csv(out/'group_split_manifest.csv', frozen_manifest)

    def fit(ids, forbidden, phase):
        ids = sorted(ids)
        e3.require(len(ids)==len(set(ids)) and not set(ids)&set(forbidden), 'Fit overlap')
        # Fresh, unfitted instance of the exact primary Exp3 preprocessing, never its fitted state.
        prep = e3.model_for('explicit_missing', cfg).named_steps['preprocess']
        settings = dict(config['mlp']); settings['hidden_layer_sizes'] = tuple(settings['hidden_layer_sizes'])
        model = Pipeline([('preprocess',prep),('model',MLPClassifier(**settings))])
        X = e3.matrix(ids,groups,cfg)
        y = np.array([mapped[g]['disease_present'] for g in ids])
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter('always')
            with threadpool_limits(limits=1): model.fit(X,y)
        scaler = prep.named_transformers_['numeric']
        categorical = prep.named_transformers_['categorical']
        imputer = categorical.named_steps['imputer']; encoder = categorical.named_steps['encoder']
        net = model.named_steps['model']
        e3.require(net.out_activation_=='logistic' and net.n_outputs_==1, 'Output must be one sigmoid')
        events.append({'phase':phase, 'fit_group_ids':ids, 'fit_rows':len(ids),
            'representative_records':[int(groups[g]['representative_record']) for g in ids],
            'scaler_n':int(scaler.n_samples_seen_), 'scaler_mean':scaler.mean_.tolist(),
            'scaler_variance':scaler.var_.tolist(), 'imputer_strategy':imputer.strategy,
            'imputer_statistics':imputer.statistics_.tolist(),
            'encoder_categories':{f:a.tolist() for f,a in zip(cfg['categorical_features'],encoder.categories_)},
            'model_parameters':net.get_params(), 'iterations':int(net.n_iter_),
            'training_loss_including_regularization':float(net.loss_),
            'weight_shapes':[list(a.shape) for a in net.coefs_], 'output_activation':net.out_activation_,
            'warnings':[{'type':type(w.message).__name__,'message':str(w.message)} for w in captured]})
        print(phase, 'groups=',len(ids),'iterations=',net.n_iter_,'warnings=',len(captured),flush=True)
        return model

    folds=[]; cv_predictions=[]; cv_rows=[]
    for f in range(1,6):
        valid={g for g in dev if int(groups[g]['validation_fold'])==f}
        train=dev-valid
        model=fit(train,valid|test,f'cv_fit_{f}')
        p=e3.predictions(model,'mlp',valid,groups,mapped,cfg,f,events)
        rp=e3.expand(p,derived)
        folds.append({'fold':f,'training':e3.counts(train,groups,mapped),'validation':e3.counts(valid,groups,mapped),
                      'distinct_group':e3.metrics(p),'original_row_weighted':e3.metrics(rp)})
        cv_predictions.extend(p);cv_rows.extend(rp)
    events.append({'phase':'cv_complete_settings_locked','config_sha256':config_hash,
                   'hyperparameter_search':False,'threshold_search':False,'test_used_for_selection':False})
    e3.require(e3.sha(HERE/'model_comparison_config.json')==config_hash,'Configuration changed')
    final_model=fit(dev,test,'final_development_fit')
    # The only test inference; no further fits or design choices after this point.
    p=e3.predictions(final_model,'mlp',test,groups,mapped,cfg,0,events); rp=e3.expand(p,derived)
    joblib.dump(final_model,out/'mlp_model.joblib')
    for name,rows in [('cv_predictions',cv_predictions),('cv_row_predictions',cv_rows),('test_predictions',p),('test_row_predictions',rp)]:
        e3.write_csv(out/(name+'.csv'),rows)
    reference=e3.load(BASE/'corrected_label_baseline/corrected_label_metrics.json')['variants']['explicit_missing']
    mlp={'cv_folds':folds,'cv_summary_all_metrics':cv_summary(folds),
         'cv_out_of_fold':{'distinct_group':e3.metrics(cv_predictions),'original_row_weighted':e3.metrics(cv_rows)},
         'test':{'distinct_group':e3.metrics(p),'original_row_weighted':e3.metrics(rp)}}
    metrics={'experiment':4,'positive_class':'disease_present=1 = int(UCI num>0) = 1-original_target',
        'threshold':cfg['threshold'],'previously_inspected_holdout':True,
        'counts':{part:e3.counts(ids,groups,mapped) for part,ids in [('all',set(groups)),('development',dev),('test',test)]},
        'reference':{'source':'../corrected_label_baseline/corrected_label_metrics.json','variant':'explicit_missing',
                     'refitted':False,**reference,'cv_summary_all_metrics':cv_summary(reference['cv_folds'])},
        'mlp':mlp,'test_difference_mlp_minus_logistic':{v:{k:mlp['test'][v][k]-reference['test'][v][k] for k in MEASURES} for v in VIEWS}}
    e3.dump(out/'model_comparison_metrics.json',metrics)
    protect(config)
    e3.require(e3.sha(HERE/'model_comparison_config.json')==config_hash,'Configuration changed after test')
    events.append({'phase':'integrity_verified','protected_files':len(config['protected_sha256']),
                   'source_sha256':e3.sha(Path(config['source_path'])),'config_sha256':config_hash})
    e3.dump(out/'execution.json',events)
    e3.dump(out/'environment.json',{'python':platform.python_version(),'executable':sys.executable,
        'platform':platform.platform(),'numpy':np.__version__,'scipy':scipy.__version__,
        'scikit_learn':sklearn.__version__,'joblib':joblib.__version__, 'threadpools':threadpool_info(),
        'fit_thread_limit':1,'runner_sha256':e3.sha(Path(__file__)),'config_sha256':config_hash})
    write_report(out,metrics,config,events)
    e3.dump(out/'run_status.json',{'status':'PASS','fits':6,'test_prediction_calls':1,
        'warnings':[w for e in events for w in e.get('warnings',[])], 'protected_files_unchanged':len(config['protected_sha256']),
        'source_sha256':e3.sha(Path(config['source_path']))})

def write_report(out,m,c,events):
    lines=['# Experiment 4: controlled neural network comparison','',
        'This is a prespecified small MLP compared with the frozen Experiment 3 **explicit_missing** logistic baseline. Logistic regression was not refitted. Its alternative mode-plus-indicator pipeline was not selected as a comparator after seeing results.', '',
        '## Design and evidence','',
        'Corrected positive class: disease_present=1 = 1-original_target = int(matched UCI num>0). Original target=1 corresponds to documented absence. All 302 record correspondences were checked again against the pinned UCI evidence. Local ca=4 and thal=0 decode to NaN, then to an explicit missing category (-1) inside the pipeline. No source row or label was changed.', '',
        'Evidence and preserved dependencies: ../corrected_label_baseline/corrected_label_report.md, corrected_label_config.json, corrected_group_manifest.csv and run_corrected_label_baseline.py; ../dataset_investigation/record_correspondence.json and dataset_provenance_report.md. These establish record correspondence, not the historical transformation author\'s intent.', '',
        'Five numeric features are standardized; eight nominal features use constant missing fill and one-hot encoding with unknown categories ignored. Numeric/categorical roles remain modeling assumptions. Every fold constructs a fresh preprocessing pipeline and fits it only on its training groups. Sentinel decoding is a fixed evidence-based transformation. The saved model expects 13 columns in inherited feature order with ca=4/thal=0 already decoded to NaN.', '',
        'Fixed MLP: Dense 32 ReLU -> Dense 16 ReLU -> one sigmoid output; binary log loss with L2 alpha=1.0, L-BFGS, max_iter=2000, max_fun=50000, tol=1e-5, seed=42, threshold=0.5, no class/sample weights. L-BFGS is a full-batch optimizer; it uses training-objective convergence, not validation early stopping. L2 was set before this run. No hyperparameter, seed, epoch, threshold, or preprocessing search was performed. Architecture/parameters are also recorded in configuration.json and execution.json.', '',
        'The exact saved development/test assignment and five folds are reused; no split is regenerated. Training uses one representative per feature group. The original 1,025 rows remain intact. Row-weighted evaluation maps the same group predictions back to all corresponding source rows; it is not a second independent sample.', '',
        '## Counts','', '| Partition | Groups | Original rows | Group class 0 / 1 | Row class 0 / 1 |','|---|---:|---:|---|---|']
    for part,d in m['counts'].items():
        lines.append(f"| {part} | {d['group_count']} | {d['original_row_count']} | {d['group_class_counts']['0']} / {d['group_class_counts']['1']} | {d['row_class_counts']['0']} / {d['row_class_counts']['1']} |")
    lines+=['','## Development-only five-fold results','','Means and sample SD across folds are descriptive, not confidence intervals. All six metrics, per-fold denominators, confusion matrices and pooled MLP out-of-fold metrics are in the JSON. Pooled metrics are not averaged fold metrics.','','| Model | View | Sensitivity mean (SD) | AUC mean (SD) |','|---|---|---:|---:|']
    for name,key in [('Frozen logistic','reference'),('MLP','mlp')]:
        for v in VIEWS:
            d=m[key]['cv_summary_all_metrics'][v]
            lines.append(f"| {name} | {v} | {d['sensitivity']['mean']:.6f} ({d['sensitivity']['sample_sd']:.6f}) | {d['roc_auc']['mean']:.6f} ({d['roc_auc']['sample_sd']:.6f}) |")
    lines+=['','## Previously inspected holdout','','| Model | View | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |','|---|---|---:|---:|---:|---:|---:|---:|']
    for name,key in [('Frozen logistic','reference'),('MLP','mlp')]:
        for v in VIEWS:
            d=m[key]['test'][v]
            lines.append('| '+name+' | '+v+' | '+' | '.join(f'{d[k]:.6f}' for k in MEASURES)+' |')
    for key in ['reference','mlp']:
        for v in VIEWS:
            d=m[key]['test'][v]
            lines += ['',f"{key}, {v}: matrix **{d['confusion_matrix']}**; denominators `{json.dumps(d['denominators'])}`."]
    lines+=['','Matrices are [[TN, FP], [FN, TP]], true labels in rows and predictions in columns. Positive means the corrected UCI presence class. Undefined rates use null.','','## Interpretation','']
    for v in VIEWS:
        a=m['reference']['test'][v];b=m['mlp']['test'][v]
        improved=[k for k in MEASURES if b[k]>a[k]]
        worse=[k for k in MEASURES if b[k]<a[k]]
        lines.append(f"{v}: MLP false negatives {b['confusion_matrix'][1][0]} versus logistic {a['confusion_matrix'][1][0]}, among {b['class_counts']['1']} corrected positives. Improved observed metrics: {', '.join(improved) or 'none'}. Lower observed metrics: {', '.join(worse) or 'none'}. Exact differences are in the metrics JSON.")
    lines+=['','These are descriptive comparisons of one prespecified network/seed, not proof of statistically reliable improvement. Sensitivity and false negatives must be assessed alongside specificity and AUC; accuracy alone is insufficient. The holdout was previously inspected in multiple experiments and provenance analysis. It is not independent test performance, even though it enters no fitting, preprocessing, stopping decision or tuning in this run.', '',
        'Patient identifiers and patient independence are unknown. Acquisition route, repetition rationale, transformation history, the omitted upstream record, missingness mechanism and some units remain unresolved. Feature groups are not patient identities, and repeated rows do not increase independent evidence. No clinical validity, diagnostic ability or patient-level generalization is established. No UI was built.', '',
        '## Integrity and reproduction','',
        f"The runner checked the original source hash and all {len(c['protected_sha256'])} pre-existing output files before and after training. Execution records contain all training group IDs and fitted preprocessing statistics. All six fit warning lists are saved. See verification.json for independent metric and structural checks; the runner does not substitute for that verifier.", '',
        'See README.md for pinned dependencies, read-only verification and reproduction into a separate new directory. The reference helpers are imported with bytecode writing disabled; none of their experiment entry points run. All new outputs are confined to this experiment directory.']
    (out/'model_comparison_report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args(); out=(args.output_dir or HERE).resolve()
    if args.output_dir:
        e3.require(not out.exists(),'Reproduction destination must be new')
        out.mkdir(parents=True)
    e3.require(not (out/'model_comparison_metrics.json').exists(),'Refusing to overwrite completed run')
    try: run(e3.load(HERE/'model_comparison_config.json'),out)
    except Exception as exc:
        e3.dump(out/'run_status.json',{'status':'FAIL','error':repr(exc)})
        raise
