"""Independent verification of Experiment 3; never trains or predicts."""
import sys
sys.dont_write_bytecode=True
import csv
import hashlib
import json
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path
import joblib
import numpy as np

OUT=Path(__file__).resolve().parent; BASE=OUT.parent
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def check(ok,msg):
    if not ok:raise AssertionError(msg)


def recompute(rows):
    c=Counter((int(r['disease_present']),int(r['prediction'])) for r in rows)
    tn,fp,fn,tp=c[0,0],c[0,1],c[1,0],c[1,1]
    div=lambda a,b:a/b if b else None
    pos=[float(r['probability_disease_present']) for r in rows if r['disease_present']=='1']
    neg=[float(r['probability_disease_present']) for r in rows if r['disease_present']=='0']
    return {'n':len(rows),'class_counts':{'0':len(neg),'1':len(pos)},'confusion_matrix':[[tn,fp],[fn,tp]],
        'sensitivity':div(tp,tp+fn),'specificity':div(tn,tn+fp),'precision':div(tp,tp+fp),
        'f1':div(2*tp,2*tp+fp+fn),'accuracy':div(tp+tn,len(rows)),
        'roc_auc':div(sum((p>n)+.5*(p==n) for p in pos for n in neg),len(pos)*len(neg)),
        'denominators':{'sensitivity':tp+fn,'specificity':tn+fp,'precision':tp+fp,
            'f1':2*tp+fp+fn,'accuracy':len(rows),'roc_auc_positive_negative_pairs':len(pos)*len(neg)}}


def metrics_equal(expected,actual):
    for k,v in expected.items():
        check(np.isclose(v,actual[k],rtol=0,atol=1e-12) if isinstance(v,float) else v==actual[k],f'Metric mismatch: {k}')


def verify():
    design=load(OUT/'corrected_label_config.json');cfg=design['inherited']; source=Path(cfg['source_path'])
    check(sha(source)==cfg['source_sha256'],'Source hash mismatch')
    for name,h in design['protected_sha256'].items():check((BASE/name).is_file() and sha(BASE/name)==h,'Protected artifact changed: '+name)
    actual={str(p.relative_to(BASE)).replace('\\','/') for p in BASE.rglob('*') if p.is_file() and OUT not in p.parents}
    check(actual==set(design['protected_sha256']),'Prior artifact added or removed')
    check(cfg==load(BASE/'baseline_config.json'),'Inherited config changed')
    check(design['variants']==['explicit_missing','mode_plus_indicator'] and design['primary_variant']=='explicit_missing','Prespecified design changed')
    for entry in load(BASE/'dataset_investigation/sources/source_manifest.json'):
        check(sha(BASE/'dataset_investigation/sources'/entry['file'])==entry['sha256'],'Source snapshot hash')
    raw=read(source);manifest=read(BASE/'group_manifest.csv');splits=read(BASE/'group_split.csv')
    groups={r['group_id']:r for r in splits};derived=read(OUT/'corrected_derived_rows.csv')
    gm=read(OUT/'corrected_group_manifest.csv')
    evidence=load(BASE/'dataset_investigation/record_correspondence.json')
    matches={r['group_id']:r for r in evidence['matched_records']}
    uci=[dict(zip(cfg['features']+['target'],r)) for r in csv.reader((BASE/'dataset_investigation/sources/uci_cleveland.data').read_text().splitlines())]
    anchors=evidence['anchor_fields'];lookup=defaultdict(list)
    for n,r in enumerate(uci,1):lookup[tuple(Decimal(r[f]) for f in anchors)].append(n)
    labels={};used=set()
    for gid,g in groups.items():
        candidates=lookup[tuple(Decimal(g[f]) for f in anchors)]
        check(candidates==[matches[gid]['uci_physical_line']],'Ambiguous UCI mapping')
        u=uci[candidates[0]-1]; used.add(candidates[0]);labels[gid]=int(int(u['target'])>0)
        check(labels[gid]==1-int(g['target']) and 0<=int(u['target'])<=4,'Corrected label does not match UCI')
        check(u==matches[gid]['uci_values_num_named_target_for_comparison'],'Saved upstream record mismatch')
        for f,code in [('ca','4'),('thal','0')]:check((g[f]==code)==(u[f]=='?'),'Sentinel mismatch')
    check(len(used)==len(groups)==302 and len(raw)==len(manifest)==len(derived)==1025,'Coverage counts')
    with source.open(newline='',encoding='utf-8-sig') as f:
        reader=csv.reader(f); next(reader); previous=reader.line_num;physical=[]
        for row in reader:physical.append((previous+1,reader.line_num));previous=reader.line_num
    for n,(r,m,d) in enumerate(zip(raw,manifest,derived),1):
        gid=m['group_id'];g=groups[gid]
        key=[cfg['features'],[r[f] for f in cfg['features']]]
        check(hashlib.sha256(json.dumps(key,separators=(',',':')).encode()).hexdigest()==gid==d['group_id'],'Group definitions changed')
        check(int(d['record_number'])==int(m['record_number'])==n,'Source record coverage')
        check((int(d['csv_line_start']),int(d['csv_line_end']))==physical[n-1],'Physical line mapping')
        check(d['original_target']==r['target']==m['target']==g['target'],'Original label altered')
        check(int(d['disease_present'])==labels[gid] and int(d['uci_num'])==int(uci[int(d['uci_line'])-1]['target']),'Derived UCI label')
        check(int(d['uci_line'])==matches[gid]['uci_physical_line'],'Derived upstream line')
        check(d['partition']==m['partition']==g['partition'] and d['validation_fold']==m['validation_fold']==g['validation_fold'],'Split/folds changed')
        for f in cfg['features']:
            missing=(f=='ca' and r[f]=='4') or (f=='thal' and r[f]=='0')
            check(d[f]==('' if missing else r[f]),'Derived feature changed beyond declared sentinel decoding')
        check(d['original_ca']==r['ca'] and d['original_thal']==r['thal'],'Raw sentinel columns lost')
        check(int(d['ca_missing'])==int(r['ca']=='4') and int(d['thal_missing'])==int(r['thal']=='0'),'Missingness flags')
    check(Counter(r['group_id'] for r in derived)==Counter(m['group_id'] for m in manifest),'Rows lost or duplicated')
    check(len(gm)==302 and {r['group_id'] for r in gm}==set(groups),'Derived group manifest coverage')
    for r in gm:
        g=groups[r['group_id']]
        check(all(r[k]==v for k,v in g.items()) and int(r['disease_present'])==labels[r['group_id']],'Derived group assignments')
    dev={g for g,r in groups.items() if r['partition']=='development'};test=set(groups)-dev
    check(len(dev)==241 and len(test)==61 and not dev&test,'Saved split')
    check({r['group_id'] for r in read(BASE/'test_predictions.csv')}==test,'Holdout not identical to primary')
    events=load(OUT/'corrected_label_execution.json');expected=['design_frozen']
    for variant in design['variants']:
        for f in range(1,6):expected += [f'cv_fit_{f}','validation_prediction']
    expected += ['all_cv_complete']
    for variant in design['variants']:expected += ['final_development_fit','test_prediction']
    expected += ['integrity_verified']
    check([e['phase'] for e in events]==expected,'Unexpected fits, predictions, or order')
    check(events[0]['config_sha256']==events[-1]['config_sha256']==sha(OUT/'corrected_label_config.json'),'Design changed after freezing')
    check(not events[0]['selection'] and not next(e for e in events if e['phase']=='all_cv_complete')['selection'],'Unexpected selection')
    fits=[e for e in events if 'fit_group_ids' in e]
    check(len(fits)==12,'Expected 10 CV and 2 final fits')
    for e in fits:
        ids=e['fit_group_ids'];fold=int(e['phase'].split('_')[-1]) if e['phase'].startswith('cv_fit_') else 0
        valid={g for g in dev if fold and int(groups[g]['validation_fold'])==fold}
        check(ids==sorted(dev-valid) and not set(ids)&(valid|test),'Forbidden training groups')
        check(len(ids)==len(set(ids))==e['fit_rows'],'Training not one row per group')
        check(e['representative_records']==[int(groups[g]['representative_record']) for g in ids],'Wrong representatives')
        X=np.array([[float(groups[g][f]) for f in cfg['features']] for g in ids])
        for f,code in [('ca',4),('thal',0)]:
            col=cfg['features'].index(f);X[X[:,col]==code,col]=np.nan
        ni=[cfg['features'].index(f) for f in cfg['numeric_features']];ci=[cfg['features'].index(f) for f in cfg['categorical_features']]
        check(e['scaler_n']==len(ids) and np.allclose(X[:,ni].mean(0),e['scaler_mean']) and np.allclose(X[:,ni].var(0),e['scaler_variance']),'Scaler uses wrong rows')
        cats=X[:,ci].copy();stats=[]
        for col in range(len(ci)):
            observed=cats[~np.isnan(cats[:,col]),col];frequencies=Counter(observed)
            check(len(observed)>0,'Entire categorical column missing: requires review')
            value=-1.0 if e['variant']=='explicit_missing' else min(frequencies,key=lambda x:(-frequencies[x],x))
            stats.append(value);cats[np.isnan(cats[:,col]),col]=value
        check(np.allclose(stats,e['imputer_statistics']),'Imputer not fit on training rows')
        check(e['imputer_strategy']==('constant' if e['variant']=='explicit_missing' else 'most_frequent'),'Imputation policy changed')
        for i,f in enumerate(cfg['categorical_features']):check(np.unique(cats[:,i]).tolist()==e['encoder_categories'][f],'Encoder learned unexpected categories')
        check(4.0 not in e['encoder_categories']['ca'] and 0.0 not in e['encoder_categories']['thal'],'Undecoded sentinels treated as valid codes')
        check(e['missing_flags_columns']==(['ca','thal'] if e['variant']=='mode_plus_indicator' else []),'Missing-indicator policy')
        check(e['missing_counts']=={f:int(np.isnan(X[:,cfg['features'].index(f)]).sum()) for f in ['ca','thal']},'Missing counts')
        check(e['class_counts']==dict(Counter(str(labels[g]) for g in ids)),'Training label counts')
        check(all(e['model_parameters'][k]==v for k,v in cfg['logistic_regression'].items()) and e['model_parameters']['random_state']==cfg['seed'],'Model settings changed')
    results=load(OUT/'corrected_label_metrics.json')
    check(results['threshold']==cfg['threshold']==.5 and results['primary_variant']=='explicit_missing','Threshold or primary choice changed')
    cvp=read(OUT/'corrected_cv_predictions.csv');cvr=read(OUT/'corrected_cv_row_predictions.csv')
    tp=read(OUT/'corrected_test_predictions.csv');tr=read(OUT/'corrected_test_row_predictions.csv')
    def validate(pred):
        for r in pred:
            check(int(r['disease_present'])==labels[r['group_id']],'Prediction target incorrect')
            check(int(r['original_target'])==1-labels[r['group_id']],'Prediction original label')
            q=float(r['probability_disease_present']);check(0<=q<=1 and int(r['prediction'])==int(q>=.5),'Threshold incorrect')
    def expansion(pred,expanded):
        lookup={r['group_id']:r for r in pred}; eligible=[m for m in manifest if m['group_id'] in lookup]
        check(Counter(int(r['record_number']) for r in expanded)==Counter(int(m['record_number']) for m in eligible),'Incomplete row expansion')
        for r in expanded:
            check(all(r[k]==v for k,v in lookup[r['group_id']].items()),'Expanded predictions differ')
            m=manifest[int(r['record_number'])-1];check(all(r[k]==m[k] for k in ['group_id','csv_line_start','csv_line_end']),'Expanded line mismatch')
    def count(ids):
        return {'group_count':len(ids),'original_row_count':sum(int(groups[g]['original_row_count']) for g in ids),
            'group_class_counts':{str(c):sum(labels[g]==c for g in ids) for c in (0,1)},
            'row_class_counts':{str(c):sum(int(groups[g]['original_row_count']) for g in ids if labels[g]==c) for c in (0,1)}}
    for part,ids in [('all',set(groups)),('development',dev),('test',test)]:check(results['counts'][part]==count(ids),'Partition counts')
    for variant in design['variants']:
        cv=[r for r in cvp if r['variant']==variant];testp=[r for r in tp if r['variant']==variant];testr=[r for r in tr if r['variant']==variant]
        check(Counter(r['group_id'] for r in cv)==Counter(dev),'CV group coverage')
        check(Counter(r['group_id'] for r in testp)==Counter(test),'Test group coverage')
        validate(cv);validate(testp);expansion(testp,testr)
        for fold in results['variants'][variant]['cv_folds']:
            f=fold['fold'];p=[r for r in cv if int(r['fold'])==f];rp=[r for r in cvr if r['variant']==variant and int(r['fold'])==f]
            valid={g for g in dev if int(groups[g]['validation_fold'])==f}
            check({r['group_id'] for r in p}==valid,'CV assignment mismatch');expansion(p,rp)
            metrics_equal(recompute(p),fold['distinct_group']);metrics_equal(recompute(rp),fold['original_row_weighted'])
            check(fold['training']==count(dev-valid) and fold['validation']==count(valid),'Fold counts')
        for view in ['distinct_group','original_row_weighted']:
            v=[f[view]['roc_auc'] for f in results['variants'][variant]['cv_folds']];summary=results['variants'][variant]['cv_summary'][view]
            check(np.isclose(np.mean(v),summary['mean_auc']) and np.isclose(np.std(v,ddof=1),summary['sample_sd_auc']),'CV summaries')
        metrics_equal(recompute(testp),results['variants'][variant]['test']['distinct_group'])
        metrics_equal(recompute(testr),results['variants'][variant]['test']['original_row_weighted'])
        event=[e for e in events if e['phase']=='test_prediction' and e['variant']==variant]
        check(len(event)==1 and event[0]['calls']==1 and event[0]['group_ids']==sorted(test),'Test prediction count')
        model=joblib.load(OUT/f'{variant}_model.joblib');prep=model.named_steps['preprocess']
        final=next(e for e in fits if e['variant']==variant and e['phase']=='final_development_fit')
        check(model.named_steps['model'].get_params()==final['model_parameters'],'Serialized model settings')
        check(prep.named_transformers_['numeric'].n_samples_seen_==241 and np.allclose(prep.named_transformers_['numeric'].mean_,final['scaler_mean']),'Serialized scaler')
        cat=prep.named_transformers_['categorical']
        check(np.allclose(cat.named_steps['imputer'].statistics_,final['imputer_statistics']),'Serialized imputer')
        for f,v in zip(cfg['categorical_features'],cat.named_steps['encoder'].categories_):check(v.tolist()==final['encoder_categories'][f],'Serialized encoder')
        if variant=='mode_plus_indicator':check(prep.named_transformers_['missing_flags'].features_.tolist()==[0,1],'Fixed missing indicators')
    for name,h in design['protected_sha256'].items():check(sha(BASE/name)==h,'Protected artifact changed during verification')
    check(sha(source)==cfg['source_sha256'],'Source changed during verification')
    return {'status':'PASS','errors':[],'source_sha256':sha(source),'protected_files_unchanged':len(design['protected_sha256']),
        'mapping_groups_verified':302,'derived_rows_verified':1025,'ambiguous_matches':0,
        'checks':['Exact UCI mapping and source/evidence checksum validation',
            'Original labels retained; corrected labels equal int(UCI num>0)',
            'Only documented missing codes decoded; raw values and source lines retained',
            'Exact saved group definitions, split and five folds reused',
            'One representative per training group; no validation/test overlap',
            'Training-only scaler, modal/constant imputer and one-hot category checks',
            'Fixed missingness indicator columns; no sentinel codes treated as observed categories',
            'Frozen logistic settings and threshold; no variant selection',
            'Independent CV/test metrics, confusion matrices, denominators and pairwise ROC-AUC',
            'Complete original-row expansion of identical group predictions',
            'One test prediction call per prespecified variant; serialized pipeline checks',
            'Original CSV and every prior output file unchanged'],
        'no_training_or_prediction_in_verifier':True,
        'scope':'Evidence checks inspect upstream labels for semantics; fitting uses development labels only. Execution traces show all CV precedes test predictions and no test-dependent settings. The holdout is previously inspected, not independent.'}


if __name__=='__main__':
    try:result=verify()
    except Exception as e:result={'status':'FAIL','errors':[f'{type(e).__name__}: {e}']}
    (OUT/'corrected_label_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2));sys.exit(0 if result['status']=='PASS' else 1)
