import json
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
ROOT = BACKEND.parent
CONTRACT = json.loads((BACKEND / 'model_contract.json').read_text(encoding='utf-8'))
FEATURES = tuple(CONTRACT['features'])
MODEL_PATH = ROOT / CONTRACT['artifact_relative_path']
THRESHOLD = CONTRACT['threshold']
DISCLAIMER = 'This is a research prototype and is not a medical diagnosis.'
