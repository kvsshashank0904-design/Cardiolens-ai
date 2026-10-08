"""Experiment 4B: one predetermined larger iteration cap; never run previous mains."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
import platform
import warnings
from unittest.mock import patch
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
    prior_config=e3.load(BASE/'model_comparison/model_comparison_config.json')
    expected=dict(prior_config['mlp']);expected['max_iter']=10000
    e3.require(config['mlp']==expected and config['threshold']==prior_config['threshold'],'Only iteration allowance may change')
    design = e3.load(BASE/'corrected_label_baseline/corrected_label_config.json')
    cfg, groups, mapped, derived = e3.checked_inputs(design)
    frozen_manifest = e3.read_csv(BASE/'corrected_label_baseline/corrected_group_manifest.csv')
    for g in frozen_manifest:
        e3.require(int(g['disease_present']) == mapped[g['group_id']]['disease_present'], 'Corrected label differs')
    dev = {g for g,r in groups.items() if r['partition']=='development'}
    test = set(groups)-dev
    e3.require(len(dev)==241 and len(test)==61 and not dev & test, 'Split changed')
    config_hash = e3.sha(HERE/'mlp_convergence_config.json')
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
        optimizer_records=[]
        original_minimize=scipy.optimize.minimize
        def capture_minimize(*args,**kwargs):
            result=original_minimize(*args,**kwargs)
            optimizer_records.append({'success':bool(result.success),'status':int(result.status),
                'message':str(result.message),'nit':int(result.nit),'nfev':int(result.nfev),
                'njev':int(result.njev),'fun':float(result.fun),
                'gradient_max_abs':float(np.max(np.abs(result.jac))),
                'method':kwargs.get('method'),'options':kwargs.get('options')})
            return result
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter('always')
            with threadpool_limits(limits=1), patch('sklearn.neural_network._multilayer_perceptron.scipy.optimize.minimize', side_effect=capture_minimize):
                model.fit(X,y)
        e3.require(len(optimizer_records)==1,'Expected one optimizer call per fit')
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
            'optimizer':optimizer_records[0],
            'converged':optimizer_records[0]['success'] and optimizer_records[0]['status']==0,
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
    e3.require(e3.sha(HERE/'mlp_convergence_config.json')==config_hash,'Configuration changed')
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
    metrics={'experiment':'4B','positive_class':'disease_present=1 = int(UCI num>0) = 1-original_target',
        'threshold':cfg['threshold'],'previously_inspected_holdout':True,
        'counts':{part:e3.counts(ids,groups,mapped) for part,ids in [('all',set(groups)),('development',dev),('test',test)]},
        'reference':{'source':'../corrected_label_baseline/corrected_label_metrics.json','variant':'explicit_missing',
                     'refitted':False,**reference,'cv_summary_all_metrics':cv_summary(reference['cv_folds'])},
        'mlp':mlp,'test_difference_mlp_minus_logistic':{v:{k:mlp['test'][v][k]-reference['test'][v][k] for k in MEASURES} for v in VIEWS}}
    previous=e3.load(BASE/'model_comparison/model_comparison_metrics.json')['mlp']
    metrics['frozen_mlp']={'source':'../model_comparison/model_comparison_metrics.json','refitted':False,**previous}
    metrics['convergence']=[{k:e[k] for k in ['phase','iterations','training_loss_including_regularization','optimizer','converged','warnings']} for e in events if 'fit_group_ids' in e]
    metrics['all_five_cv_folds_converged']=all(e['converged'] for e in metrics['convergence'][:5])
    metrics['cv_difference_vs_frozen']={key:{v:{k:mlp['cv_summary_all_metrics'][v][k]['mean']-metrics[key]['cv_summary_all_metrics'][v][k]['mean'] for k in MEASURES} for v in VIEWS} for key in ['reference','frozen_mlp']}
    e3.dump(out/'mlp_convergence_metrics.json',metrics)
    protect(config)
    e3.require(e3.sha(HERE/'mlp_convergence_config.json')==config_hash,'Configuration changed after test')
    events.append({'phase':'integrity_verified','protected_files':len(config['protected_sha256']),
                   'source_sha256':e3.sha(Path(config['source_path'])),'config_sha256':config_hash})
    e3.dump(out/'execution.json',events)
    e3.dump(out/'environment.json',{'python':platform.python_version(),'executable':sys.executable,
        'platform':platform.platform(),'numpy':np.__version__,'scipy':scipy.__version__,
        'scikit_learn':sklearn.__version__,'joblib':joblib.__version__, 'threadpools':threadpool_info(),
        'fit_thread_limit':1,'runner_sha256':e3.sha(Path(__file__)),'config_sha256':config_hash})
    write_report(out,metrics,config,events)
    e3.dump(out/'run_status.json',{'status':('PASS' if all(e.get('converged',True) and not e.get('warnings',[]) for e in events) else 'COMPLETED_WITH_WARNINGS'),'fits':6,'test_prediction_calls':1,
        'warnings':[w for e in events for w in e.get('warnings',[])], 'protected_files_unchanged':len(config['protected_sha256']),
        'source_sha256':e3.sha(Path(config['source_path']))})

def write_report(out,m,c,events):
    from report_convergence import write_report as render
    render(out,m,c,events)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args(); out=(args.output_dir or HERE).resolve()
    if args.output_dir:
        e3.require(not out.exists(),'Reproduction destination must be new')
        out.mkdir(parents=True)
    e3.require(not (out/'mlp_convergence_metrics.json').exists(),'Refusing to overwrite completed run')
    try: run(e3.load(HERE/'mlp_convergence_config.json'),out)
    except Exception as exc:
        e3.dump(out/'run_status.json',{'status':'FAIL','error':repr(exc)})
        raise
