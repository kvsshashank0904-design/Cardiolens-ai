"""Independent artifact verification; no model training or prediction calls."""
import sys
sys.dont_write_bytecode=True
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import joblib
import numpy as np

OUT=Path(__file__).resolve().parent
PRIMARY=OUT.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, parent=OUT):
    return json.loads((parent/name).read_text(encoding='utf-8'))


def csv_rows(path):
    with path.open(newline='',encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def recompute(rows):
    cells=Counter((int(r['target']),int(r['prediction'])) for r in rows)
    tn,fp,fn,tp=(cells[0,0],cells[0,1],cells[1,0],cells[1,1])
    div=lambda a,b: a/b if b else None
    pos=[float(r['probability_target_1']) for r in rows if int(r['target'])==1]
    neg=[float(r['probability_target_1']) for r in rows if int(r['target'])==0]
    return {'n':len(rows),'class_counts':{'0':len(neg),'1':len(pos)},
        'confusion_matrix':[[tn,fp],[fn,tp]],'sensitivity':div(tp,tp+fn),
        'specificity':div(tn,tn+fp),'precision':div(tp,tp+fp),'f1':div(2*tp,2*tp+fp+fn),
        'accuracy':div(tp+tn,len(rows)),
        'roc_auc':div(sum((p>n)+0.5*(p==n) for p in pos for n in neg),len(pos)*len(neg)),
        'denominators':{'sensitivity':tp+fn,'specificity':tn+fp,'precision':tp+fp,
                        'f1':2*tp+fp+fn,'accuracy':len(rows),'roc_auc_positive_negative_pairs':len(pos)*len(neg)}}


def equal_metrics(expected, actual):
    for k,v in expected.items():
        require(np.isclose(v,actual[k],atol=1e-12,rtol=0) if isinstance(v,float) else v==actual[k],f'Metric mismatch: {k}')


def expand(predictions, manifest):
    mapping={r['group_id']:r for r in predictions}
    return [{**m,**{k:mapping[m['group_id']][k] for k in ['target','prediction','probability_target_1']}}
            for m in manifest if m['group_id'] in mapping]


def verify():
    design=load('repetition_weighted_config.json'); cfg=design['primary_config']
    source=Path(cfg['source_path'])
    require(sha(source)==cfg['source_sha256']==design['source_sha256'],'Source hash changed')
    for name,digest in design['primary_file_sha256'].items():
        require((PRIMARY/name).is_file() and sha(PRIMARY/name)==digest,'Primary file changed: '+name)
    current={str(p.relative_to(PRIMARY)).replace('\\','/') for p in PRIMARY.rglob('*') if p.is_file() and OUT not in p.parents}
    require(current==set(design['primary_file_sha256']),'Primary files added or removed')
    require(cfg==load('baseline_config.json',PRIMARY),'Inherited configuration changed')
    require(cfg['threshold']==0.5 and design['model']=='logistic_regression','Design not frozen')
    manifest=csv_rows(PRIMARY/'group_manifest.csv'); splits=csv_rows(PRIMARY/'group_split.csv')
    source_rows=csv_rows(source); groups={r['group_id']:r for r in splits}
    require(len(source_rows)==len(manifest)==1025 and len(groups)==len(splits)==302,'Incomplete mapping')
    physical=[]
    with source.open(newline='',encoding='utf-8-sig') as f:
        reader=csv.reader(f); next(reader); previous=reader.line_num
        for row in reader:
            physical.append((previous+1,reader.line_num)); previous=reader.line_num
    for n,(r,m) in enumerate(zip(source_rows,manifest),1):
        gid=hashlib.sha256(json.dumps([cfg['features'],[r[f] for f in cfg['features']]],separators=(',',':')).encode()).hexdigest()
        require(gid==m['group_id'] and int(m['record_number'])==n,'Source-row-to-feature-group mismatch')
        require((int(m['csv_line_start']),int(m['csv_line_end']))==physical[n-1],'Line mapping changed')
        require(r['target']==m['target']==groups[gid]['target'],'Label consistency failed')
        require(all(r[f]==groups[gid][f] for f in cfg['features']),'Group feature key mismatch')
        require(all(m[f]==groups[gid][f] for f in ['partition','validation_fold']),'Primary fold/partition mismatch')
    require(Counter(m['group_id'] for m in manifest)==Counter({g:int(r['original_row_count']) for g,r in groups.items()}),'Group multiplicities changed')
    dev={g for g,r in groups.items() if r['partition']=='development'}
    test={g for g,r in groups.items() if r['partition']=='test'}
    require(len(dev)==241 and len(test)==61 and not dev&test,'Invalid saved split')
    old_test=csv_rows(PRIMARY/'test_predictions.csv')
    require({r['group_id'] for r in old_test}==test,'Test groups do not match primary')
    events=load('repetition_weighted_execution.json')
    phases=[e['phase'] for e in events]
    expected=['design_frozen']
    for f in range(1,6): expected += [f'cv_fit_{f}','validation_prediction']
    expected += ['cv_complete','final_development_fit','test_prediction','integrity_verified']
    require(phases==expected,'Unexpected execution ordering or extra prediction/fitting phase')
    require(events[0]['config_sha256']==sha(OUT/'repetition_weighted_config.json')==events[-1]['config_sha256'],'Design changed across execution')
    fit_events=[e for e in events if 'training_record_numbers' in e]
    require(len(fit_events)==6,'Expected five CV fits and one final fit')
    for e in fit_events:
        fold=int(e['phase'].split('_')[-1]) if e['phase'].startswith('cv_fit_') else None
        valid={g for g in dev if fold and int(groups[g]['validation_fold'])==fold}
        eligible=dev-valid
        wanted=[i for i,m in enumerate(manifest,1) if m['group_id'] in eligible]
        require(e['training_record_numbers']==wanted,'Missing, extra, repeated, or reordered training source rows')
        require(len(wanted)==len(set(wanted))==e['training_row_count'],'Every eligible source row must occur exactly once')
        require(set(e['training_group_ids'])==eligible and not eligible&(test|valid),'Train/validation/test overlap')
        counts=Counter(manifest[i-1]['group_id'] for i in wanted)
        require(dict(counts)==e['group_multiplicities'],'Repeated training records not retained exactly')
        require(all(counts[g]==int(groups[g]['original_row_count']) for g in eligible),'Training multiplicity differs from source')
        require(e['training_group_count']==len(eligible),'Training group count')
        X=np.array([[float(source_rows[i-1][f]) for f in cfg['features']] for i in wanted])
        y=[int(source_rows[i-1]['target']) for i in wanted]
        h=hashlib.sha256(json.dumps({'X':X.tolist(),'y':y,'records':wanted},separators=(',',':')).encode()).hexdigest()
        require(h==e['training_data_sha256'],'Actual fitted feature/label inputs changed')
        ni=[cfg['features'].index(f) for f in cfg['numeric_features']]
        require(e['scaler_n_samples_seen']==len(wanted),'Scaler used wrong number of rows')
        require(np.allclose(X[:,ni].mean(axis=0),e['scaler_mean']) and np.allclose(X[:,ni].var(axis=0),e['scaler_variance']),'Preprocessing not learned on corresponding expanded training rows')
        for f in cfg['categorical_features']:
            require(sorted(set(X[:,cfg['features'].index(f)]))==e['learned_categories'][f],'Encoder categories differ from training-only values')
        require(all(e['model_parameters'][k]==v for k,v in cfg['logistic_regression'].items()),'Logistic regression settings changed')
        require(e['model_parameters']['random_state']==cfg['seed'],'Random seed changed')
        require(e['training_class_counts']=={str(c):y.count(c) for c in (0,1)},'Training class counts')
    predictions=csv_rows(OUT/'repetition_weighted_cv_predictions.csv')
    cv_row_predictions=csv_rows(OUT/'repetition_weighted_cv_row_predictions.csv')
    cv=load('repetition_weighted_cv_metrics.json')
    require(Counter(r['group_id'] for r in predictions)==Counter(dev),'CV group coverage')
    require(Counter(int(r['record_number']) for r in cv_row_predictions)==Counter(int(m['record_number']) for m in manifest if m['group_id'] in dev),'CV original-row coverage')
    def validate_predictions(p):
        for r in p:
            require(int(r['target'])==int(groups[r['group_id']]['target']),'Prediction target mismatch')
            q=float(r['probability_target_1'])
            require(0<=q<=1 and int(r['prediction'])==int(q>=0.5),'Probability/threshold mismatch')
    validate_predictions(predictions)
    def check_expansion(p, expanded):
        required=expand(p,manifest)
        by_record={int(r['record_number']):r for r in expanded}
        require(len(by_record)==len(expanded)==len(required),'Expanded prediction count')
        for r in required:
            saved=by_record[int(r['record_number'])]
            require(all(str(saved[k])==str(r[k]) for k in ['csv_line_start','csv_line_end','group_id','target','prediction','probability_target_1']),'Expanded prediction differs from group prediction')
    for f in cv['folds']:
        number=f['fold']; p=[r for r in predictions if int(r['fold'])==number]
        rp=[r for r in cv_row_predictions if int(r['fold'])==number]
        valid={g for g in dev if int(groups[g]['validation_fold'])==number}
        require({r['group_id'] for r in p}==set(f['validation_group_ids'])==valid,'CV folds differ from primary')
        require(set(f['training_group_ids'])==dev-valid,'CV train groups differ')
        check_expansion(p,rp)
        equal_metrics(recompute(p),f['distinct_group']); equal_metrics(recompute(rp),f['original_row_weighted'])
        for label,ids in [('training',dev-valid),('validation',valid)]:
            rr=[m for m in manifest if m['group_id'] in ids]
            expected_count={'groups':len(ids),'original_rows':len(rr),
                'group_class_counts':{str(c):sum(int(groups[g]['target'])==c for g in ids) for c in (0,1)},
                'row_class_counts':{str(c):sum(int(r['target'])==c for r in rr) for c in (0,1)}}
            require(f[label]==expected_count,'CV counts mismatch')
    for view in ['distinct_group','original_row_weighted']:
        values=[f[view]['roc_auc'] for f in cv['folds']]
        require(np.isclose(np.mean(values),cv['summary'][view]['mean_roc_auc']) and np.isclose(np.std(values,ddof=1),cv['summary'][view]['sample_sd_roc_auc']),'CV mean/SD mismatch')
    tp=csv_rows(OUT/'repetition_weighted_test_predictions.csv'); tr=csv_rows(OUT/'repetition_weighted_test_row_predictions.csv')
    require(Counter(r['group_id'] for r in tp)==Counter(test),'Test must predict each primary test group exactly once')
    require(events[-2]['group_ids']==sorted(test) and events[-2]['prediction_calls']==1,'Test prediction call trace')
    validate_predictions(tp); check_expansion(tp,tr)
    m=load('repetition_weighted_metrics.json')
    equal_metrics(recompute(tp),m['distinct_group']); equal_metrics(recompute(tr),m['original_row_weighted'])
    require(set(m['test_group_ids'])==test,'Metrics test groups')
    primary_metrics=load('baseline_metrics.json',PRIMARY)
    require(m['counts']['development']==primary_metrics['counts']['development'] and m['counts']['test']==primary_metrics['counts']['test'],'Counts differ across experiments')
    cmp=load('repetition_weighted_comparison.json')
    for view in ['distinct_group','original_row_weighted']:
        for k,d in cmp['test_differences'][view].items():
            require(d['primary']==primary_metrics[view][k] and d['repetition_weighted']==m[view][k],'Comparison values mismatch')
            require(np.isclose(d['signed_difference'],m[view][k]-primary_metrics[view][k]) and np.isclose(d['absolute_difference'],abs(m[view][k]-primary_metrics[view][k])),'Comparison differences mismatch')
    old_cv=[r for r in csv_rows(PRIMARY/'cv_predictions.csv') if r['candidate']=='logistic_regression']
    for f in cmp['primary_cv_derived_from_saved_predictions']:
        p=[r for r in old_cv if int(r['fold'])==f['fold']]
        equal_metrics(recompute(p),f['distinct_group']); equal_metrics(recompute(expand(p,manifest)),f['original_row_weighted'])
    for view in ['distinct_group','original_row_weighted']:
        values=[f[view]['roc_auc'] for f in cmp['primary_cv_derived_from_saved_predictions']]
        require(np.isclose(np.mean(values),cmp['primary_cv_summary'][view]['mean_roc_auc']) and np.isclose(np.std(values,ddof=1),cmp['primary_cv_summary'][view]['sample_sd_roc_auc']),'Primary derived summary')
    # Inspect serialized preprocessing without making another test prediction.
    model=joblib.load(OUT/'repetition_weighted_model.joblib')
    final=fit_events[-1]; pre=model.named_steps['preprocess']
    require(pre.named_transformers_['numeric'].n_samples_seen_==811,'Serialized scaler fit size')
    require(np.allclose(pre.named_transformers_['numeric'].mean_,final['scaler_mean']),'Serialized scaler means')
    require(np.allclose(pre.named_transformers_['numeric'].var_,final['scaler_variance']),'Serialized scaler variance')
    require(model.named_steps['model'].get_params()==final['model_parameters'],'Serialized model parameters')
    for name,values in zip(cfg['categorical_features'],pre.named_transformers_['categorical'].categories_):
        require(values.tolist()==final['learned_categories'][name],'Serialized encoder categories')
    require(pre.named_transformers_['categorical'].handle_unknown=='ignore' and pre.named_transformers_['categorical'].drop is None,'Encoding policy changed')
    require(sha(source)==design['source_sha256'],'Source changed during verification')
    for name,h in design['primary_file_sha256'].items(): require(sha(PRIMARY/name)==h,'Primary changed during verification')
    return {'status':'PASS','errors':[], 'source_sha256':sha(source),
        'primary_files_checked':len(design['primary_file_sha256']), 'source_and_primary_unchanged':True,
        'checks':['Exact original row-to-feature-group mapping, physical lines and consistent labels',
            'Exact saved partition/fold reuse; no split regenerated',
            'Every eligible source row included once; all original multiplicities retained',
            'Zero validation/test group overlap in each fit',
            'Scaler mean/variance/count and encoder categories match expanded training rows only',
            'Fixed logistic parameters, seed and threshold; six fits and no model selection',
            'CV complete before final fit; exactly one test prediction call on distinct groups',
            'Same held-out group IDs as primary; group predictions correctly expanded to original rows',
            'Independent CV/test confusion matrices, denominators, metrics and pairwise ROC-AUC',
            'Primary CV weighted view derived from saved predictions; comparison deltas checked',
            'Serialized final pipeline matches final training trace'],
        'scope':'Dataflow and execution trace show no test label/score passed to fitting or selection; labels are read for mapping integrity and final scoring. This is an exploratory shared holdout, not an independent test.',
        'no_models_retrained_or_predictions_generated_by_verifier':True}


if __name__=='__main__':
    try:
        result=verify()
    except Exception as exc:
        result={'status':'FAIL','errors':[f'{type(exc).__name__}: {exc}']}
    (OUT/'repetition_weighted_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    sys.exit(0 if result['status']=='PASS' else 1)
