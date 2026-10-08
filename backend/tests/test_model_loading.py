import hashlib
import json
from pathlib import Path
from unittest.mock import patch
import joblib
import pytest
from fastapi.testclient import TestClient
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from backend.app.config import ROOT, BACKEND, MODEL_PATH
from backend.app.main import create_app
from backend.app.model_service import ModelLoadError


def test_one_load_no_training_or_refit(monkeypatch,payload):
    def forbidden(*args,**kwargs):
        raise AssertionError('Training/refitting is forbidden')
    for cls in [Pipeline,ColumnTransformer,StandardScaler,OneHotEncoder,SimpleImputer,LogisticRegression]:
        for name in ['fit','fit_transform','partial_fit']:
            if hasattr(cls,name):monkeypatch.setattr(cls,name,forbidden)
    with patch('backend.app.model_service.joblib.load',wraps=joblib.load) as loader:
        with TestClient(create_app()) as client:
            service=client.app.state.model_service
            before=joblib.hash(service.pipeline)
            for _ in range(3):assert client.post('/predict',json=payload).status_code==200
            assert client.get('/health').json()['model_loaded']
            assert loader.call_count==1
            assert joblib.hash(service.pipeline)==before


@pytest.mark.parametrize('mode',['missing','corrupt'])
def test_loading_failure(mode):
    failure = {'side_effect':FileNotFoundError('private/path')} if mode=='missing' else {'return_value':b'not a model'}
    with patch('backend.app.model_service.Path.read_bytes',**failure):
        with pytest.raises(ModelLoadError) as caught:
            with TestClient(create_app()):pass
    assert 'private/path' not in str(caught.value)
    assert 'Frozen Experiment 3' in str(caught.value)


def test_inference_error_is_sanitized(client,payload,monkeypatch):
    def broken(*args,**kwargs):raise RuntimeError('C:/private/path stack trace')
    monkeypatch.setattr(client.app.state.model_service.pipeline,'predict_proba',broken)
    r=client.post('/predict',json=payload)
    assert r.status_code==500
    assert r.json()=={'detail':'Prediction could not be completed.'}


def test_all_protected_files_unchanged():
    m=json.loads((BACKEND/'protected_manifest.json').read_text())
    assert hashlib.sha256(Path(m['source_path']).read_bytes()).hexdigest()==m['source_sha256']
    for name,h in m['protected_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,name
