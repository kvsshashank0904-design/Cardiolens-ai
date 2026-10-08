import json
import math
import numpy as np
import pytest
from backend.app.config import FEATURES
from backend.app.schemas import PredictionRequest
from backend.app.model_service import ModelService


def test_recorded_predictions_and_explanations(client,recorded_cases):
    # Integration parity only: no evaluation/tuning or metric selection.
    assert len(recorded_cases)==61
    for payload, recorded in recorded_cases:
        response=client.post('/predict',json=payload)
        assert response.status_code==200, response.text
        d=response.json()
        assert d['prediction']==int(recorded['prediction'])
        assert d['model_probability']==pytest.approx(float(recorded['probability_disease_present']),abs=1e-12)
        assert d['disclaimer']=='This is a research prototype and is not a medical diagnosis.'
        assert d['model']['experiment']=='Experiment 3'
        e=d['explanation']
        score=e['intercept']+sum(x['contribution'] for x in e['feature_contributions'])
        assert score==pytest.approx(e['log_odds'],abs=1e-12)
        assert 1/(1+math.exp(-score))==pytest.approx(d['model_probability'],abs=1e-12)
        assert 'numeric__age' in [x['feature'] for x in e['feature_contributions']]


def test_determinism_and_order(client,payload):
    before=client.post('/predict',json=payload).json()
    after=client.post('/predict',json=dict(reversed(list(payload.items())))).json()
    assert before==after==client.post('/predict',json=payload).json()
    X,_=ModelService.matrix(PredictionRequest(**payload))
    assert list(PredictionRequest.model_fields)==list(FEATURES)
    for i,f in enumerate(FEATURES):
        assert X[0,i]==payload[f] or (np.isnan(X[0,i]) and f in ['ca','thal'])


def test_explicit_missing(client,payload):
    payload.update(ca=4,thal=0)
    X,missing=ModelService.matrix(PredictionRequest(**payload))
    assert missing==['ca','thal'] and np.isnan(X[0,11:13]).all()
    d=client.post('/predict',json=payload).json()
    assert d['missing_features']==['ca','thal']
    names=[x['feature'] for x in d['explanation']['feature_contributions']]
    assert 'categorical__ca_-1.0' in names and 'categorical__thal_-1.0' in names


@pytest.mark.parametrize('field,value',[
    ('age','54'),('age',True),('age',-1),('age',78),('chol',None),
    ('cp',4),('ca',5),('ca',-1),('thal',4),('sex',True),('sex',1.0),('oldpeak',-1),('unknown',5)])
def test_invalid_values(client,payload,field,value):
    payload[field]=value
    r=client.post('/predict',json=payload)
    assert r.status_code==422
    assert r.json()['detail']
    assert 'Traceback' not in r.text and 'C:' not in r.text


@pytest.mark.parametrize('raw',['{','[]','null','{"age":NaN}','{"age":Infinity}'])
def test_malformed_or_nonfinite(client,raw):
    r=client.post('/predict',content=raw,headers={'content-type':'application/json'})
    assert r.status_code==422 and r.json()['detail']


def test_missing_field(client,payload):
    del payload['age']
    r=client.post('/predict',json=payload)
    assert r.status_code==422
    assert any(e['location']==['body','age'] and e['type']=='missing' for e in r.json()['detail'])


def test_numeric_json_integers(client,payload):
    payload['age']=int(payload['age'])
    assert client.post('/predict',json=payload).status_code==200
