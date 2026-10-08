"""Experiment 3. Only this directory is writable; prior artifacts are read-only inputs.
Run with the existing pinned Python environment and -B. No split or tuning is performed.
"""
import sys
sys.dont_write_bytecode = True
import csv
import hashlib
import json
import platform
import warnings
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

import joblib
import numpy as np
import scipy
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.exceptions import ConvergenceWarning
from sklearn.impute import SimpleImputer, MissingIndicator
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
sys.path.insert(0,str(BASE))
from run_baseline import score, require, dump, write_csv


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path): return json.loads(path.read_text(encoding='utf-8'))
def read_csv(path):
    with path.open(newline='',encoding='utf-8-sig') as f: return list(csv.DictReader(f))


def integrity(design):
    require(sha(Path(design['inherited']['source_path']))==design['inherited']['source_sha256'],'Source changed')
    for name,h in design['protected_sha256'].items():
        require((BASE/name).is_file() and sha(BASE/name)==h,'Protected file changed: '+name)


def checked_inputs(design):
    integrity(design)
    cfg=design['inherited']
    require(cfg==load(BASE/'baseline_config.json'),'Inherited settings changed')
    for s in load(BASE/'dataset_investigation/sources/source_manifest.json'):
        require(sha(BASE/'dataset_investigation/sources'/s['file'])==s['sha256'],'Evidence snapshot changed')
    source=read_csv(Path(cfg['source_path']))
    manifest=read_csv(BASE/'group_manifest.csv')
    split=read_csv(BASE/'group_split.csv'); groups={r['group_id']:r for r in split}
    evidence=load(BASE/'dataset_investigation/record_correspondence.json')
    match={r['group_id']:r for r in evidence['matched_records']}
    require(len(source)==len(manifest)==1025 and len(groups)==len(split)==len(match)==302,'Unexpected counts')
    uci=[dict(zip(cfg['features']+['target'],r)) for r in csv.reader((BASE/'dataset_investigation/sources/uci_cleveland.data').read_text().splitlines())]
    anchors=evidence['anchor_fields']; lookup=defaultdict(list)
    key=lambda r:tuple(Decimal(r[f]) for f in anchors)
    for n,r in enumerate(uci,1):lookup[key(r)].append(n)
    mapped={}; used=set()
    for gid,g in groups.items():
        m=match[gid]; candidate=lookup[key(g)]
        require(candidate==[m['uci_physical_line']],'Ambiguous upstream correspondence; stop')
        u=uci[candidate[0]-1]; used.add(candidate[0])
        require(all(m['local_values'][f]==g[f] for f in cfg['features']+['target']),'Evidence differs from saved group')
        require(u==m['uci_values_num_named_target_for_comparison'],'UCI evidence mismatch')
        corrected=int(int(u['target'])>0)
        require(int(u['target']) in range(5) and corrected==1-int(g['target']),'Ambiguous target mapping; stop')
        for field,code in design['missing_codes'].items():
            require((float(g[field])==code)==(u[field]=='?'),'Missing-code evidence disagrees; stop')
        mapped[gid]={'disease_present':corrected,'uci_num':int(u['target']),'uci_line':candidate[0]}
    require(len(used)==302,'Nonunique upstream matches')
    derived=[]
    for n,(r,m) in enumerate(zip(source,manifest),1):
        gid=m['group_id']; g=groups[gid]
        calculated=hashlib.sha256(json.dumps([cfg['features'],[r[f] for f in cfg['features']]],separators=(',',':')).encode()).hexdigest()
        require(calculated==gid and int(m['record_number'])==n,'Source mapping mismatch')
        require(r['target']==m['target']==g['target'],'Source/group label mismatch')
        require(all(r[f]==g[f] for f in cfg['features']),'Source/group feature mismatch')
        require(all(m[f]==g[f] for f in ['partition','validation_fold']),'Split/fold mismatch')
        transformed={f:('' if f in design['missing_codes'] and float(r[f])==design['missing_codes'][f] else r[f]) for f in cfg['features']}
        derived.append({'record_number':n,'csv_line_start':m['csv_line_start'],'csv_line_end':m['csv_line_end'],
            'group_id':gid,'partition':g['partition'],'validation_fold':g['validation_fold'],
            'original_target':int(r['target']),**mapped[gid],
            'original_ca':r['ca'],'original_thal':r['thal'],
            'ca_missing':int(r['ca']=='4'),'thal_missing':int(r['thal']=='0'),**transformed})
    require(Counter(r['group_id'] for r in derived)==Counter({g:int(r['original_row_count']) for g,r in groups.items()}),'Lost/repeated source records')
    return cfg,groups,mapped,derived


def matrix(ids,groups,cfg):
    X=np.array([[float(groups[g][f]) for f in cfg['features']] for g in ids])
    for f,code in [('ca',4),('thal',0)]:
        i=cfg['features'].index(f); X[X[:,i]==code,i]=np.nan
    return X


def model_for(variant,cfg):
    ni=[cfg['features'].index(f) for f in cfg['numeric_features']]
    ci=[cfg['features'].index(f) for f in cfg['categorical_features']]
    imputer=SimpleImputer(strategy='constant',fill_value=-1,keep_empty_features=True) if variant=='explicit_missing' else SimpleImputer(strategy='most_frequent',keep_empty_features=True)
    categorical=Pipeline([('imputer',imputer),('encoder',OneHotEncoder(handle_unknown='ignore',sparse_output=False,drop=None))])
    transformers=[('numeric',StandardScaler(),ni),('categorical',categorical,ci)]
    if variant=='mode_plus_indicator':
        transformers.append(('missing_flags',MissingIndicator(features='all'),[cfg['features'].index(f) for f in ['ca','thal']]))
    return Pipeline([('preprocess',ColumnTransformer(transformers,remainder='drop')),
        ('model',LogisticRegression(random_state=cfg['seed'],**cfg['logistic_regression']))])


def fit(variant,ids,forbidden,groups,mapped,cfg,phase,events):
    ids=sorted(ids)
    require(len(ids)==len(set(ids)) and not set(ids)&set(forbidden),'Training overlap')
    X=matrix(ids,groups,cfg);y=np.array([mapped[g]['disease_present'] for g in ids])
    model=model_for(variant,cfg)
    with warnings.catch_warnings():
        warnings.simplefilter('error',ConvergenceWarning)
        model.fit(X,y)
    prep=model.named_steps['preprocess'];cat=prep.named_transformers_['categorical']
    ni=[cfg['features'].index(f) for f in cfg['numeric_features']]
    ci=[cfg['features'].index(f) for f in cfg['categorical_features']]
    sc=prep.named_transformers_['numeric'];im=cat.named_steps['imputer'];enc=cat.named_steps['encoder']
    require(sc.n_samples_seen_==len(ids) and np.allclose(sc.mean_,X[:,ni].mean(axis=0)),'Training-only scaler check failed')
    values=im.transform(X[:,ci])
    require(all(np.array_equal(v,np.unique(values[:,i])) for i,v in enumerate(enc.categories_)),'Training-only encoder check failed')
    events.append({'phase':phase,'variant':variant,'fit_group_ids':ids,'fit_rows':len(ids),
        'representative_records':[int(groups[g]['representative_record']) for g in ids],
        'class_counts':dict(Counter(map(str,y.tolist()))),'scaler_n':int(sc.n_samples_seen_),
        'scaler_mean':sc.mean_.tolist(),'scaler_variance':sc.var_.tolist(),
        'imputer_strategy':im.strategy,'imputer_statistics':im.statistics_.tolist(),
        'missing_counts':{f:int(np.isnan(X[:,cfg['features'].index(f)]).sum()) for f in ['ca','thal']},
        'encoder_categories':{f:v.tolist() for f,v in zip(cfg['categorical_features'],enc.categories_)},
        'missing_flags_columns':['ca','thal'] if variant=='mode_plus_indicator' else [],
        'model_parameters':model.named_steps['model'].get_params(),
        'iterations':model.named_steps['model'].n_iter_.tolist()})
    return model


def predictions(model,variant,ids,groups,mapped,cfg,fold,events):
    ids=sorted(ids); require(len(ids)==len(set(ids)),'Duplicate prediction group')
    q=model.predict_proba(matrix(ids,groups,cfg))[:,list(model.classes_).index(1)]
    events.append({'phase':'test_prediction' if fold==0 else 'validation_prediction',
        'variant':variant,'fold':fold,'group_ids':ids,'calls':1})
    return [{'variant':variant,'fold':fold,'group_id':g,'disease_present':mapped[g]['disease_present'],
        'original_target':int(groups[g]['target']),'prediction':int(p>=cfg['threshold']),
        'probability_disease_present':float(p),'original_row_count':int(groups[g]['original_row_count'])} for g,p in zip(ids,q)]


def expand(pred,derived):
    by={r['group_id']:r for r in pred}
    return [{**by[r['group_id']],**{f:r[f] for f in ['record_number','csv_line_start','csv_line_end']}}
            for r in derived if r['group_id'] in by]


def metrics(rows):
    return score(np.array([r['disease_present'] for r in rows]),np.array([r['prediction'] for r in rows]),
                 np.array([r['probability_disease_present'] for r in rows]))


def counts(ids,groups,mapped):
    return {'group_count':len(ids),'original_row_count':sum(int(groups[g]['original_row_count']) for g in ids),
        'group_class_counts':{str(c):sum(mapped[g]['disease_present']==c for g in ids) for c in (0,1)},
        'row_class_counts':{str(c):sum(int(groups[g]['original_row_count']) for g in ids if mapped[g]['disease_present']==c) for c in (0,1)}}


def main():
    design=load(OUT/'corrected_label_config.json');frozen=sha(OUT/'corrected_label_config.json')
    cfg,groups,mapped,derived=checked_inputs(design)
    write_csv(OUT/'corrected_derived_rows.csv',derived)
    write_csv(OUT/'corrected_group_manifest.csv',[{**g,'group_id':gid,'original_target':g['target'],**mapped[gid]} for gid,g in groups.items()])
    dump(OUT/'transformation_evidence.json',{'status':'PASS','groups_checked':302,'source_rows_checked':1025,
        'mapping':'disease_present = int(UCI num>0) = 1-original_target',
        'label_mapping_counts':{'original_0_to_presence_1_groups':138,'original_1_to_absence_0_groups':164},
        'missing_codes':design['missing_codes'],'evidence_sha256':sha(BASE/'dataset_investigation/record_correspondence.json'),
        'uci_sha256':sha(BASE/'dataset_investigation/sources/uci_cleveland.data'),'ambiguous_matches':0,
        'derived_blank_ca':sum(r['ca_missing'] for r in derived),'derived_blank_thal':sum(r['thal_missing'] for r in derived)})
    dev={g for g,r in groups.items() if r['partition']=='development'};test=set(groups)-dev
    require(len(dev)==241 and len(test)==61 and not dev&test,'Invalid reused split')
    events=[{'phase':'design_frozen','config_sha256':frozen,'variants':design['variants'],'selection':False}]
    results={};cv_pred=[];cv_row_pred=[]
    for variant in design['variants']:
        folds=[]
        for f in range(1,6):
            valid={g for g in dev if int(groups[g]['validation_fold'])==f}; train=dev-valid
            model=fit(variant,train,valid|test,groups,mapped,cfg,f'cv_fit_{f}',events)
            p=predictions(model,variant,valid,groups,mapped,cfg,f,events);rp=expand(p,derived)
            folds.append({'fold':f,'training':counts(train,groups,mapped),'validation':counts(valid,groups,mapped),
                'distinct_group':metrics(p),'original_row_weighted':metrics(rp)})
            cv_pred.extend(p);cv_row_pred.extend(rp)
        results[variant]={'cv_folds':folds,'cv_summary':{v:{'mean_auc':float(np.mean([x[v]['roc_auc'] for x in folds])),
            'sample_sd_auc':float(np.std([x[v]['roc_auc'] for x in folds],ddof=1))} for v in ['distinct_group','original_row_weighted']}}
    events.append({'phase':'all_cv_complete','config_sha256':frozen,'selection':False})
    # Both variants were specified before training; no holdout-driven selection.
    require(sha(OUT/'corrected_label_config.json')==frozen,'Configuration changed')
    test_pred=[];test_rows=[]
    for variant in design['variants']:
        model=fit(variant,dev,test,groups,mapped,cfg,'final_development_fit',events)
        p=predictions(model,variant,test,groups,mapped,cfg,0,events);rp=expand(p,derived)
        results[variant]['test']={'distinct_group':metrics(p),'original_row_weighted':metrics(rp)}
        joblib.dump(model,OUT/f'{variant}_model.joblib')
        test_pred.extend(p);test_rows.extend(rp)
    for name,data in [('cv_predictions',cv_pred),('cv_row_predictions',cv_row_pred),('test_predictions',test_pred),('test_row_predictions',test_rows)]:
        write_csv(OUT/f'corrected_{name}.csv',data)
    report_metrics={'positive_class':'disease_present=1 means matched UCI num in 1..4; 0 means UCI num=0',
        'primary_variant':design['primary_variant'],'model':'logistic_regression','threshold':cfg['threshold'],
        'previously_inspected_holdout':True,'counts':{'all':counts(set(groups),groups,mapped),
        'development':counts(dev,groups,mapped),'test':counts(test,groups,mapped)},'variants':results}
    dump(OUT/'corrected_label_metrics.json',report_metrics)
    integrity(design); require(sha(OUT/'corrected_label_config.json')==frozen,'Configuration changed after test')
    events.append({'phase':'integrity_verified','protected_files':len(design['protected_sha256']),
        'source_sha256':sha(Path(cfg['source_path'])),'config_sha256':frozen})
    dump(OUT/'corrected_label_execution.json',events)
    dump(OUT/'corrected_label_environment.json',{'python':platform.python_version(),'numpy':np.__version__,
        'scipy':scipy.__version__,'sklearn':sklearn.__version__,'joblib':joblib.__version__,
        'config_sha256':frozen,'runner_sha256':sha(Path(__file__)),'source_sha256':sha(Path(cfg['source_path'])),
        'primary_helper_sha256':sha(BASE/'run_baseline.py')})
    lines=['# Experiment 3: corrected-label baseline','','## Design and evidence','',
        'The label transformation is **disease_present = 1 - original_target = int(matched UCI num > 0)**. All 302 saved feature groups were independently matched to unique UCI records using the eight unchanged anchor fields, then checked against the saved record-level evidence. Every source row retains its original label alongside the new label. No ambiguous matches were found.', '',
        'Local ca=4 and thal=0 were verified in both directions against UCI missing entries. Only in the derived data, these codes become blanks/NaN. The derived file retains original_ca, original_thal, original_target, missingness flags, source record/physical line numbers, UCI num/line, and saved group/partition/fold IDs. All 1,025 original rows remain represented. No patient identifier is inferred.', '',
        'Evidence: ../dataset_investigation/record_correspondence.json; ../dataset_investigation/dataset_provenance_report.md; the pinned UCI snapshot and codebook under ../dataset_investigation/sources/. Public sources: [UCI documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/heart-disease.names) and [processed Cleveland records](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data). The record correspondence overrides contradictory publisher prose for this derived experiment; it does not establish the historical transformation author\'s intent.', '',
        '## Fixed design and necessary changes','',
        '- Fixed: existing feature group IDs, seed 42, saved development/test assignments and five folds; one first-occurrence row per training group; logistic regression L2/C=1/lbfgs/max_iter=2000/tol=0.0001/no class weights; numeric scaling, nominal one-hot feature roles, unknown-category handling, and threshold 0.5.',
        '- Changed: positive-label direction; ca/thal sentinel decoding; categorical missing-value preprocessing. Logistic regression is fixed rather than reselecting between models. The earlier majority model is not rerun. No hyperparameter or threshold search.',
        '- Primary option explicit_missing: replace NaN by -1 inside the categorical pipeline and one-hot encode it as explicitly missing. It is never described as a valid vessel count or defect state. This retains missingness without guessing its hidden value.',
        '- Sensitivity option mode_plus_indicator: learn the modal category from training groups only, fill NaN with it, and append two fixed ca/thal missingness indicators. Modes are assumptions, not recovered measurements. Missing indicators exist even if a training fold has no missing entry.',
        '- All learned transformations fit only within each fold\'s training data. Constant decoding uses documented codes, not fitted statistics. New model inputs must decode the two sentinels to NaN before using the saved pipelines.',
        '- Both options were specified before fitting. Both are reported without choosing a winner from final test results. The missingness mechanism remains unknown; comparing these options is not proof that either is correct.', '',
        'The original grouping remains fixed even if transformed inputs coincide. This preserves the same feature-pattern separation as the earlier experiments, not patient-level independence.', '',
        '## Counts and results','','| Partition | Groups | Original rows | Corrected group labels 0 / 1 | Corrected row labels 0 / 1 |','|---|---:|---:|---|---|']
    for part,c in report_metrics['counts'].items():
        lines.append(f"| {part} | {c['group_count']} | {c['original_row_count']} | {c['group_class_counts']['0']} / {c['group_class_counts']['1']} | {c['row_class_counts']['0']} / {c['row_class_counts']['1']} |")
    lines+=['','Final fitting uses 241 representative rows; test evaluation uses 61 groups or their 214 original rows. No repeated-row training is added in Experiment 3. Fold counts and both metric views are in corrected_label_metrics.json.','','| Option | CV view | Mean AUC | Fold sample SD |','|---|---|---:|---:|']
    for variant,r in results.items():
        for view,m in r['cv_summary'].items():lines.append(f"| {variant} | {view} | {m['mean_auc']:.6f} | {m['sample_sd_auc']:.6f} |")
    lines+=['','| Option | Test view | Sensitivity | Specificity | Precision | F1 | Accuracy | ROC-AUC |','|---|---|---:|---:|---:|---:|---:|---:|']
    for variant,r in results.items():
        for view,m in r['test'].items():
            lines.append('| '+variant+' | '+view+' | '+' | '.join('undefined' if m[k] is None else f'{m[k]:.6f}' for k in ['sensitivity','specificity','precision','f1','accuracy','roc_auc'])+' |')
    for variant,r in results.items():
        for view,m in r['test'].items():
            lines+=['',f"**{variant}, {view}:** confusion matrix `{m['confusion_matrix']}`; denominators `{m['denominators']}`."]
    lines+=['','Matrices are [[TN, FP], [FN, TP]] with rows=true 0/1, columns=predicted 0/1. Sensitivity now refers to the matched UCI presence class; specificity to the absence class. ROC-AUC uses probability_disease_present. Undefined metrics are null. CV mean/SD describe five folds and are not confidence intervals. Row-weighted metrics expand the same group predictions, without another prediction call.', '',
        '## What these results mean','',
        'Earlier sensitivities concerned the opposite numeric class and cannot be compared directly as disease-presence sensitivities. Reversing binary labels and probability direction alone need not change discrimination or accuracy; changes in those measures can also reflect the missing-data treatment. No improvement claim is made from corrected terminology.', '',
        'The holdout has been inspected in earlier experiments and in provenance analysis. This is a secondary exploratory, shared-holdout comparison, not independent test performance. Upstream label values were consulted for semantic validation, not model/threshold selection. No test rows enter fitting or learned preprocessing.', '',
        'Unknowns remain: acquisition route, transformation/repetition history, missingness mechanism, one absent UCI record, some units, and patient linkage. The derived positive class follows documented UCI outcome coding; it is not a newly validated clinical diagnosis. These results establish no clinical validity, patient-level generalization, or performance on new patients. Repetition is not independent evidence. No UI was built.', '',
        '## Verification and reproduction','',
        'Run the separate verifier after this script. corrected_label_verification.json records PASS/FAIL and explicit errors; it reconstructs mappings and metrics independently. Config contains frozen hashes for every pre-existing output, including both experiments and provenance files. Source checksum is checked before and after.', '',
        'Use Python 3.12 with the unchanged ../baseline_requirements.txt pins. From the workspace root:', '',
        '```powershell','& work/baseline-env/Scripts/python.exe -B outputs/corrected_label_baseline/run_corrected_label_baseline.py',
        '& work/baseline-env/Scripts/python.exe -B outputs/corrected_label_baseline/verify_corrected_label_baseline.py','```', '',
        'Reruns regenerate only this experiment\'s outputs; they are reproductions, not new independent tests. The saved pipelines require features in inherited order with documented sentinels decoded to NaN. Only load trusted serialized models.']
    (OUT/'corrected_label_report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    dump(OUT/'corrected_label_run_status.json',{'status':'PASS','errors':[],'convergence_errors':0,'protected_files_unchanged':len(design['protected_sha256'])})
    print(json.dumps({'status':'PASS','results':{v:{'cv':r['cv_summary'],'test':r['test']} for v,r in results.items()}},indent=2))


if __name__=='__main__':
    try:main()
    except Exception as e:
        dump(OUT/'corrected_label_run_status.json',{'status':'FAIL','errors':[f'{type(e).__name__}: {e}']})
        raise
