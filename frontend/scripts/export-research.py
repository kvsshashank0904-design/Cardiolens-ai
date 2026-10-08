"""Export aggregate frozen evidence and API schema; never fit or predict."""
import csv
import hashlib
import json
import statistics
from pathlib import Path

FRONT=Path(__file__).resolve().parents[1]
ROOT=FRONT.parent
def load(p):return json.loads((ROOT/p).read_text())
sources=['outputs/corrected_label_baseline/corrected_label_metrics.json',
         'outputs/model_comparison/model_comparison_metrics.json',
         'outputs/mlp_convergence_check/mlp_convergence_metrics.json',
         'outputs/corrected_label_baseline/corrected_test_predictions.csv',
         'backend/model_contract.json']
e3=load(sources[0]);lr=e3['variants']['explicit_missing']
e4=load(sources[1])['mlp'];e4b=load(sources[2])['mlp']
def cv(model):
    return {k:{'mean':statistics.mean(f['distinct_group'][k] for f in model['cv_folds']),
        'sd':statistics.stdev(f['distinct_group'][k] for f in model['cv_folds'])}
        for k in ['sensitivity','specificity','precision','f1','accuracy','roc_auc']}
with (ROOT/sources[3]).open() as f:rows=[r for r in csv.DictReader(f) if r['variant']=='explicit_missing']
points=[[0,0]];pos=sum(int(r['disease_present']) for r in rows);neg=len(rows)-pos
for t in sorted({float(r['probability_disease_present']) for r in rows},reverse=True):
    chosen=[r for r in rows if float(r['probability_disease_present'])>=t]
    tp=sum(int(r['disease_present']) for r in chosen);fp=len(chosen)-tp
    points.append([fp/neg,tp/pos])
data={'counts':e3['counts'],'repeated_copies':1025-302,'missing_groups':{'ca':4,'thal':2},
      'lr_test':lr['test'],'lr_cv':cv(lr),'roc_points':points,
      'runs':[{'id':label,'model':name,'cv':cv(model),'test':model['test'],'status':status} for label,name,model,status in
      [('Exp 3','Logistic regression',lr,'Frozen baseline'),('Exp 4','MLP (2,000 iterations)',e4,'2 CV warnings'),('Exp 4B','MLP (10,000 iterations)',e4b,'5 folds converged')]],
      'sources':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
(FRONT/'lib/verified-research.json').write_text(json.dumps(data,indent=2)+'\n')
contract=load('backend/model_contract.json')
public={k:contract[k] for k in ['features','numeric_features','categorical_features','numeric_supported_ranges','categorical_codes','threshold','missing_codes']}
(FRONT/'lib/input-contract.json').write_text(json.dumps(public,indent=2)+'\n')
print('Exported only aggregate recorded metrics, recorded ROC points, and input schema.')
