"""Independent metrics and structural verification; no model fitting or tuning."""
import sys
sys.dont_write_bytecode=True
import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
import joblib
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
MEASURES=['sensitivity','specificity','precision','f1','accuracy','roc_auc']
VIEWS=['distinct_group','original_row_weighted']
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):
    with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def require(ok,message):
    if not ok:raise AssertionError(message)
def same(a,b,where='value'):
    if isinstance(a,dict):
        require(set(a)==set(b),where+' keys')
        for k in a:same(a[k],b[k],where+'.'+k)
    elif isinstance(a,(list,tuple)):
        require(len(a)==len(b),where+' length')
        for i,(x,y) in enumerate(zip(a,b)):same(x,y,where+str(i))
    elif isinstance(a,(float,int)) and not isinstance(a,bool):
        require(b is not None and math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-12),where+' numeric mismatch')
    else:require(a==b,where+' mismatch')

def calculate(predictions):
    pairs=[(int(r['disease_present']),int(r['prediction']),float(r['probability_disease_present'])) for r in predictions]
    cm=[[sum(y==a and p==b for y,p,q in pairs) for b in [0,1]] for a in [0,1]]
    tn,fp=cm[0];fn,tp=cm[1]
    pos=[q for y,p,q in pairs if y==1];neg=[q for y,p,q in pairs if y==0]
    div=lambda x,y:x/y if y else None
    return {'n':len(pairs),'class_counts':{'0':len(neg),'1':len(pos)},'confusion_matrix':cm,
        'confusion_matrix_order':'rows=true [0,1], columns=predicted [0,1]',
        'sensitivity':div(tp,tp+fn),'specificity':div(tn,tn+fp),'precision':div(tp,tp+fp),
        'f1':div(2*tp,2*tp+fp+fn),'accuracy':div(tp+tn,len(pairs)),
        'roc_auc':div(sum((p>n)+0.5*(p==n) for p in pos for n in neg),len(pos)*len(neg)),
        'denominators':{'sensitivity':tp+fn,'specificity':tn+fp,'precision':tp+fp,
            'f1':2*tp+fp+fn,'accuracy':len(pairs),'roc_auc_positive_negative_pairs':len(pos)*len(neg)},
        'undefined_policy':'null if denominator is zero; ROC-AUC null if either label is absent'}

def verify(out,result):
    c=load(HERE/'mlp_convergence_config.json')
    same(c,load(out/'configuration.json'),'configuration copy')
    def integrity():
        require(digest(Path(c['source_path']))==c['source_sha256'],'Source hash changed')
        for name,h in c['protected_sha256'].items():
            require((BASE/name).is_file() and digest(BASE/name)==h,'Protected changed: '+name)
    integrity()
    result['source_sha256']=c['source_sha256'];result['protected_files_unchanged']=len(c['protected_sha256'])
    result['checks'].append('Source SHA-256 and every frozen prior output file match pre-run hashes')
    cfg=load(BASE/'baseline_config.json')
    original=rows(Path(c['source_path']));split=rows(BASE/'group_split.csv');groups={g['group_id']:g for g in split}
    manifest=rows(BASE/'group_manifest.csv')
    corrected=rows(BASE/'corrected_label_baseline/corrected_group_manifest.csv')
    same(rows(out/'group_split_manifest.csv'),corrected,'frozen corrected manifest')
    evidence=load(BASE/'dataset_investigation/record_correspondence.json')
    match={r['group_id']:r for r in evidence['matched_records']}
    uci=list(csv.reader((BASE/'dataset_investigation/sources/uci_cleveland.data').read_text().splitlines()))
    y={}
    for r in corrected:
        gid=r['group_id'];g=groups[gid];m=match[gid];u=uci[int(r['uci_line'])-1]
        require(int(r['uci_line'])==m['uci_physical_line'],'UCI line mismatch')
        require(int(r['disease_present'])==1-int(g['target'])==int(float(u[-1])>0),'Incorrect mapping')
        require(int(r['uci_num'])==int(float(u[-1])),'UCI label mismatch')
        for f in ['partition','validation_fold']+cfg['features']:require(r[f]==g[f],'Group/assignment changed')
        for f,code in [('ca',4),('thal',0)]:
            require((float(g[f])==code)==(u[cfg['features'].index(f)]=='?'),'Sentinel evidence mismatch')
        y[gid]=int(r['disease_present'])
    require(len(original)==len(manifest)==1025 and len(y)==302,'Record counts')
    for n,(r,m) in enumerate(zip(original,manifest),1):
        gid=hashlib.sha256(json.dumps([cfg['features'],[r[f] for f in cfg['features']]],separators=(',',':')).encode()).hexdigest()
        require(gid==m['group_id'] and int(m['record_number'])==n,'Raw feature grouping changed')
        require(r['target']==groups[gid]['target'],'Within-group label conflict')
    require(Counter(m['group_id'] for m in manifest)==Counter({g:int(r['original_row_count']) for g,r in groups.items()}),'Multiplicity mismatch')
    result['checks'].append('302 corrected UCI labels, missing-code evidence, raw feature hashes, 1025 row links and exact saved split/folds checked')
    dev={g for g,r in groups.items() if r['partition']=='development'};test=set(groups)-dev
    require(len(dev)==241 and len(test)==61 and not dev&test,'Development/test groups')
    events=load(out/'execution.json');fits=[e for e in events if 'fit_group_ids' in e]
    expected=['design_frozen']
    for f in range(1,6):expected += [f'cv_fit_{f}','validation_prediction']
    expected += ['cv_complete_settings_locked','final_development_fit','test_prediction','integrity_verified']
    require([e['phase'] for e in events]==expected,'Execution phase order or extra fit/predict')
    require(len(fits)==6,'Fit count')
    for e in events:
        if 'config_sha256' in e:require(e['config_sha256']==digest(HERE/'mlp_convergence_config.json'),'Config changed during run')
        if 'test_used_for_selection' in e:require(e['test_used_for_selection'] is False,'Test selection flag')
    ni=[cfg['features'].index(f) for f in cfg['numeric_features']]
    def matrix(ids):
        X=np.array([[float(groups[g][f]) for f in cfg['features']] for g in ids])
        for f,code in [('ca',4),('thal',0)]:
            col=cfg['features'].index(f); X[X[:,col]==code,col]=np.nan
        return X
    for i,e in enumerate(fits):
        valid={g for g in dev if int(groups[g]['validation_fold'])==i+1} if i<5 else set()
        train=dev-valid
        require(e['fit_group_ids']==sorted(train),'Incorrect training membership')
        require(not train&(valid|test),'Leakage in group IDs')
        require(e['fit_rows']==e['scaler_n']==len(train),'Fit count/scaler count')
        same(e['representative_records'],[int(groups[g]['representative_record']) for g in sorted(train)],'Representatives')
        X=matrix(sorted(train))
        same(e['scaler_mean'],X[:,ni].mean(axis=0).tolist(),'Training-only scaler means')
        same(e['scaler_variance'],X[:,ni].var(axis=0).tolist(),'Training-only scaler variance')
        require(e['imputer_strategy']=='constant' and e['imputer_statistics']==[-1]*8,'Missing imputation')
        cats={f:np.unique(np.nan_to_num(X[:,cfg['features'].index(f)],nan=-1)).tolist() for f in cfg['categorical_features']}
        same(e['encoder_categories'],cats,'Training-only category vocabulary')
        ninputs=5+sum(len(v) for v in cats.values())
        require(e['weight_shapes']==[[ninputs,32],[32,16],[16,1]] and e['output_activation']=='logistic','MLP architecture')
        for k,v in c['mlp'].items():same(v,e['model_parameters'][k],'fixed '+k)
        require(e['iterations']<=c['mlp']['max_iter'],'Iteration limit')
        prediction_event=events[2+i*2] if i<5 else events[-2]
        require(prediction_event['group_ids']==sorted(valid if i<5 else test),'Prediction partition')
    oldcfg=load(BASE/'model_comparison/model_comparison_config.json')
    expected=dict(oldcfg['mlp']);expected['max_iter']=10000
    same(expected,c['mlp'],'Only max_iter change allowed')
    same(oldcfg['threshold'],c['threshold'],'Fixed threshold')
    oldfits=[e for e in load(BASE/'model_comparison/execution.json') if 'fit_group_ids' in e]
    for new,old in zip(fits,oldfits):
        for k in ['fit_group_ids','representative_records','scaler_n','scaler_mean','scaler_variance','imputer_strategy','imputer_statistics','encoder_categories','weight_shapes']:
            same(old[k],new[k],'Exact Experiment 4 '+k)
        expected_parameters=dict(old['model_parameters']);expected_parameters['max_iter']=10000
        same(expected_parameters,new['model_parameters'],'All explicit and default MLP parameters')
        opt=new['optimizer']
        require(new['converged']==(opt['success'] and opt['status']==0),'Convergence flag')
        require(opt['nit']==new['iterations'],'Optimizer iteration count')
        same(opt['fun'],new['training_loss_including_regularization'],'Optimizer loss')
        require(math.isfinite(opt['fun']) and math.isfinite(opt['gradient_max_abs']),'Finite optimization state')
        require(opt['method']=='L-BFGS-B' and opt['options']['maxiter']==10000 and opt['options']['maxfun']==50000 and opt['options']['gtol']==1e-5,'Optimizer settings')
    result['all_five_cv_folds_converged']=all(e['converged'] for e in fits[:5])
    result['optimizer_statuses']=[{'phase':e['phase'],**e['optimizer']} for e in fits]
    result['checks'].append('Only max_iter changed from 2000 to 10000; all other default/explicit MLP parameters and fitted preprocessing match Experiment 4; optimizer status and loss checked')
    result['fit_warnings']=[w for e in fits for w in e['warnings']]
    result['convergence_check']={'status':'REVIEW_REQUIRED' if result['fit_warnings'] else 'PASS',
        'fits_with_warnings':[e['phase'] for e in fits if e['warnings']],
        'note':'Consult optimizer_statuses for termination success and stopping criterion. Any listed warning fits require review; an empty list means no fit warnings. Successful relative-loss termination does not imply gradient tolerance or global optimality. No retries or tuning were performed.'}
    result['checks'].append('Six fits: exact training membership, zero validation/test group overlap, training-only preprocessing, fixed MLP settings and one test inference after CV; warning lists inspected separately')
    metrics=load(out/'mlp_convergence_metrics.json')
    ref=load(BASE/'corrected_label_baseline/corrected_label_metrics.json')['variants']['explicit_missing']
    require(metrics['reference']['refitted'] is False,'Reference refitted flag')
    for k,v in ref.items():same(v,metrics['reference'][k],'Frozen logistic reference')
    frozen=load(BASE/'model_comparison/model_comparison_metrics.json')['mlp']
    for k,v in frozen.items():same(v,metrics['frozen_mlp'][k],'Frozen Experiment 4 MLP')
    require(metrics['frozen_mlp']['refitted'] is False,'Frozen MLP refit flag')
    require(metrics['all_five_cv_folds_converged']==result['all_five_cv_folds_converged'],'Convergence summary')
    same(metrics['convergence'],[{k:e[k] for k in ['phase','iterations','training_loss_including_regularization','optimizer','converged','warnings']} for e in fits],'Optimization metrics')
    for key in ['reference','frozen_mlp']:
        for v in VIEWS:
            same({k:metrics['mlp']['cv_summary_all_metrics'][v][k]['mean']-metrics[key]['cv_summary_all_metrics'][v][k]['mean'] for k in MEASURES},metrics['cv_difference_vs_frozen'][key][v],'CV comparison')
    def check_predictions(ps,rs,ids):
        require(len(ps)==len(ids) and {r['group_id'] for r in ps}==ids,'Prediction group coverage')
        by={r['group_id']:r for r in ps}
        for gid,r in by.items():
            q=float(r['probability_disease_present'])
            require(math.isfinite(q) and 0<=q<=1 and int(r['prediction'])==int(q>=c['threshold']),'Probability/threshold')
            require(int(r['disease_present'])==y[gid] and int(r['original_target'])==int(groups[gid]['target']),'Prediction label')
            require(int(r['original_row_count'])==int(groups[gid]['original_row_count']),'Prediction multiplicity')
            require(int(r['fold'])==(int(groups[gid]['validation_fold']) if gid in dev else 0),'Prediction fold')
        expected_rows=[r for r in manifest if r['group_id'] in ids]
        require(len(rs)==len(expected_rows),'Row count')
        for row,m in zip(rs,expected_rows):
            for k in ['record_number','csv_line_start','csv_line_end']:require(row[k]==m[k],'Physical row links')
            for k,v in by[m['group_id']].items():require(row[k]==v,'Expanded prediction mismatch')
    for key,directory,prefix,variant in [('mlp',out,'',None),('reference',BASE/'corrected_label_baseline','corrected_','explicit_missing'),('frozen_mlp',BASE/'model_comparison','',None)]:
        cv=rows(directory/(prefix+'cv_predictions.csv'));cr=rows(directory/(prefix+'cv_row_predictions.csv'))
        tp=rows(directory/(prefix+'test_predictions.csv'));tr=rows(directory/(prefix+'test_row_predictions.csv'))
        if variant:
            cv,cr,tp,tr=[[r for r in a if r['variant']==variant] for a in [cv,cr,tp,tr]]
        # Row expansion is source-ordered within each fold, as saved by both runners.
        for fold in range(1,6):
            ps=[r for r in cv if int(r['fold'])==fold];rs=[r for r in cr if int(r['fold'])==fold]
            valid={g for g in dev if int(groups[g]['validation_fold'])==fold}
            check_predictions(ps,rs,valid)
            for v,data in zip(VIEWS,[ps,rs]):same(calculate(data),metrics[key]['cv_folds'][fold-1][v],f'{key} CV {fold} {v}')
        check_predictions(tp,tr,test)
        for v,data in zip(VIEWS,[tp,tr]):same(calculate(data),metrics[key]['test'][v],f'{key} test {v}')
        for v in VIEWS:
            for k in MEASURES:
                values=[f[v][k] for f in metrics[key]['cv_folds']]
                same({'mean':float(np.mean(values)),'sample_sd':float(np.std(values,ddof=1))},metrics[key]['cv_summary_all_metrics'][v][k],'CV mean/SD')
        if key=='mlp':
            for v,data in zip(VIEWS,[cv,cr]):same(calculate(data),metrics[key]['cv_out_of_fold'][v],'pooled OOF')
    for v in VIEWS:
        same({k:metrics['mlp']['test'][v][k]-metrics['reference']['test'][v][k] for k in MEASURES},metrics['test_difference_mlp_minus_logistic'][v],'Metric differences')
    result['checks'].append('All three models: all five CV folds and test metrics independently recomputed by direct counts and pairwise AUC, including original-row expansion, denominators and differences')
    for part,ids in [('all',set(groups)),('development',dev),('test',test)]:
        counts={'group_count':len(ids),'original_row_count':sum(int(groups[g]['original_row_count']) for g in ids),
            'group_class_counts':{str(k):sum(y[g]==k for g in ids) for k in [0,1]},
            'row_class_counts':{str(k):sum(int(groups[g]['original_row_count']) for g in ids if y[g]==k) for k in [0,1]}}
        same(counts,metrics['counts'][part],'Partition counts')
    # Independent forward calculation through the saved final network; no fitting or tuning.
    model=joblib.load(out/'mlp_model.joblib'); prep=model.named_steps['preprocess'];net=model.named_steps['model']
    require(list(model.classes_)==[0,1] and net.activation=='relu' and net.out_activation_=='logistic','Saved network classes/activations')
    same([list(a.shape) for a in net.coefs_],fits[-1]['weight_shapes'],'Saved shapes')
    same(prep.named_transformers_['numeric'].mean_.tolist(),fits[-1]['scaler_mean'],'Saved scaler')
    require(prep.named_transformers_['numeric'].n_samples_seen_==241,'Saved scaler sample count')
    ids=sorted(test);X=matrix(ids)
    scaler=prep.named_transformers_['numeric'];cat=prep.named_transformers_['categorical']
    same(cat.named_steps['imputer'].statistics_.tolist(),[-1]*8,'Saved missing imputer')
    require(cat.named_steps['encoder'].handle_unknown=='ignore','Unknown-category policy')
    blocks=[(X[:,ni]-scaler.mean_)/scaler.scale_]
    for f,values in zip(cfg['categorical_features'],cat.named_steps['encoder'].categories_):
        same(values.tolist(),fits[-1]['encoder_categories'][f],'Saved categories')
        col=np.nan_to_num(X[:,cfg['features'].index(f)],nan=-1)
        blocks.append(np.array([col==v for v in values],dtype=float).T)
    a=np.column_stack(blocks)
    for weight,bias in zip(net.coefs_[:-1],net.intercepts_[:-1]):a=np.maximum(0,a@weight+bias)
    logits=(a@net.coefs_[-1]+net.intercepts_[-1]).ravel()
    probabilities=1/(1+np.exp(-logits))
    saved={r['group_id']:float(r['probability_disease_present']) for r in rows(out/'test_predictions.csv')}
    require(np.allclose(probabilities,[saved[g] for g in ids],rtol=1e-10,atol=1e-12),'Saved network probabilities')
    result['checks'].append('Saved model architecture, preprocessing and test probabilities independently checked with explicit matrix multiplication and sigmoid')
    env=load(out/'environment.json')
    require(env['runner_sha256']==digest(HERE/'run_mlp_convergence.py'),'Runner hash mismatch')
    require(env['config_sha256']==digest(HERE/'mlp_convergence_config.json'),'Configuration hash mismatch')
    integrity()
    result['checks'].append('Source and protected hashes rechecked at verification completion')
    result['status']='PASS_WITH_WARNINGS' if result['fit_warnings'] or not all(e['converged'] for e in fits) else 'PASS'
    result['new_artifact_sha256']={p.name:digest(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='verification.json'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--results-dir',type=Path,default=HERE)
    args=parser.parse_args();out=args.results_dir.resolve()
    result={'status':'FAIL','errors':[],'checks':[], 'no_fitting_or_tuning_in_verifier':True,
        'scope':'Recomputed saved metrics and manually evaluated the saved final model. Membership/statistic checks plus execution trace and fixed code support no train/validation/test leakage in this run; the holdout is previously inspected and not independent.'}
    try:verify(out,result)
    except Exception as exc:result['errors'].append(repr(exc))
    (out/'verification.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='new_artifact_sha256'},indent=2))
    sys.exit(0 if result['status'] in ['PASS','PASS_WITH_WARNINGS'] else 1)
