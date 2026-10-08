from backend.app.config import FEATURES

def test_health(client):
    r=client.get('/health')
    assert r.status_code==200
    assert r.json()=={'status':'ok','service':'CardioLens AI','model_loaded':True}

def test_model_info(client):
    r=client.get('/model-info')
    assert r.status_code==200
    d=r.json()
    assert d['experiment']=='Experiment 3' and d['threshold']==0.5
    assert d['features']==list(FEATURES)
    assert d['label_mapping']=={'0':'UCI-mapped absence','1':'UCI-mapped presence'}
    assert d['missing_codes']=={'ca':4,'thal':0}
    assert 'C:' not in r.text and 'joblib' not in r.text

def test_openapi(client):
    schema=client.get('/openapi.json').json()
    assert set(schema['paths'])=={'/health','/model-info','/predict'}
    assert schema['components']['schemas']['PredictionRequest']['required']==list(FEATURES)
