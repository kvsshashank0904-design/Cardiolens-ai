"""Load a checksum-pinned fitted pipeline. No fit, train or model construction."""
import hashlib
import io
from importlib.metadata import version
from pathlib import Path
import joblib
import numpy as np
from scipy.special import expit
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from .config import CONTRACT, FEATURES, MODEL_PATH, THRESHOLD, DISCLAIMER
from .schemas import PredictionRequest, PredictionResponse, ModelMetadata, Explanation, FeatureContribution


class ModelLoadError(RuntimeError):
    pass


class InferenceError(RuntimeError):
    pass


class ModelService:
    def __init__(self, artifact_path: Path = MODEL_PATH):
        try:
            for library, expected in CONTRACT['runtime_versions'].items():
                if version(library) != expected:
                    raise ValueError('Incompatible runtime')
            data = Path(artifact_path).read_bytes()
            if hashlib.sha256(data).hexdigest() != CONTRACT['artifact_sha256']:
                raise ValueError('Artifact integrity mismatch')
            # Deserialize only the bytes whose checksum was checked.
            self.pipeline = joblib.load(io.BytesIO(data))
            self._validate_contract()
        except Exception:
            raise ModelLoadError('Frozen Experiment 3 model could not be loaded or validated. Check the local installation and artifact integrity.') from None

    def _validate_contract(self):
        p = self.pipeline
        if not isinstance(p, Pipeline) or list(p.named_steps) != ['preprocess', 'model']:
            raise ValueError('Pipeline structure')
        prep = p.named_steps['preprocess']; model = p.named_steps['model']
        if not isinstance(model, LogisticRegression) or list(p.classes_) != [0,1] or p.n_features_in_ != 13:
            raise ValueError('Model class contract')
        expected = {'C':1.0,'penalty':'l2','solver':'lbfgs','max_iter':2000,'tol':0.0001,'class_weight':None,'random_state':42}
        if any(model.get_params()[k] != v for k,v in expected.items()):
            raise ValueError('Model parameters')
        ni = [FEATURES.index(f) for f in CONTRACT['numeric_features']]
        ci = [FEATURES.index(f) for f in CONTRACT['categorical_features']]
        if list(prep.transformers_[0][2]) != ni or list(prep.transformers_[1][2]) != ci:
            raise ValueError('Feature index contract')
        cat = prep.named_transformers_['categorical']
        imputer = cat.named_steps['imputer']; encoder = cat.named_steps['encoder']
        if imputer.strategy != 'constant' or imputer.fill_value != -1 or encoder.handle_unknown != 'ignore' or encoder.drop is not None:
            raise ValueError('Missing/encoding contract')
        if int(prep.named_transformers_['numeric'].n_samples_seen_) != 241:
            raise ValueError('Frozen training count')
        self.transformed_names = prep.get_feature_names_out(list(FEATURES)).tolist()
        if len(self.transformed_names) != len(model.coef_[0]):
            raise ValueError('Coefficient dimension')
        self.positive_index = list(p.classes_).index(1)

    @staticmethod
    def matrix(request: PredictionRequest):
        values = request.model_dump()
        missing = [f for f,code in CONTRACT['missing_codes'].items() if values[f] == code]
        X = np.array([[np.nan if f in missing else values[f] for f in FEATURES]], dtype=float)
        return X, missing

    def predict(self, request: PredictionRequest) -> PredictionResponse:
        try:
            X, missing = self.matrix(request)
            probability = float(self.pipeline.predict_proba(X)[0,self.positive_index])
            prep = self.pipeline.named_steps['preprocess']; model = self.pipeline.named_steps['model']
            transformed = prep.transform(X)[0]
            contributions = transformed * model.coef_[0]
            intercept = float(model.intercept_[0]); score = float(intercept + contributions.sum())
            if not np.isfinite(probability) or not np.all(np.isfinite(contributions)) or not np.isclose(expit(score),probability,rtol=1e-12,atol=1e-12):
                raise ValueError('Explanation/probability mismatch')
            prediction = int(probability >= THRESHOLD)
            return PredictionResponse(prediction=prediction,
                prediction_label=('Model prediction: disease presence' if prediction else 'Model prediction: disease absence'),
                model_probability=probability, model=ModelMetadata(), missing_features=missing,
                explanation=Explanation(intercept=intercept,log_odds=score,
                    feature_contributions=[FeatureContribution(feature=f,contribution=float(v)) for f,v in zip(self.transformed_names,contributions)]),
                disclaimer=DISCLAIMER)
        except Exception:
            raise InferenceError('Prediction could not be completed.') from None
