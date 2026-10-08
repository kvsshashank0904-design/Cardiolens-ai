import csv
import json
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from backend.app.config import ROOT, FEATURES, CONTRACT
from backend.app.main import create_app


def read_csv(path):
    with path.open(newline='',encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope='session')
def recorded_cases():
    folder=ROOT/'outputs/corrected_label_baseline'
    groups={r['group_id']:r for r in read_csv(folder/'corrected_group_manifest.csv')}
    predictions=[r for r in read_csv(folder/'corrected_test_predictions.csv') if r['variant']=='explicit_missing']
    return [( {f:(int(groups[r['group_id']][f]) if f in CONTRACT['categorical_features'] else float(groups[r['group_id']][f])) for f in FEATURES}, r) for r in predictions]


@pytest.fixture
def payload(recorded_cases):
    return dict(recorded_cases[0][0])


@pytest.fixture
def client():
    with TestClient(create_app()) as c:
        yield c
