from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field
from .config import CONTRACT


def numeric(name):
    low, high = CONTRACT['numeric_supported_ranges'][name]
    return Field(strict=True, allow_inf_nan=False, ge=low, le=high,
                 description='Supported prototype range from frozen CSV; not a clinical validity range.')


def category(name):
    codes = CONTRACT['categorical_codes'][name]
    assert codes == list(range(min(codes), max(codes)+1))
    return Field(strict=True, ge=min(codes), le=max(codes),
                 description=f'Local CSV integer codes {codes}; ca=4 and thal=0 mean missing.')


class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    age: Annotated[float, numeric('age')]
    sex: Annotated[int, category('sex')]
    cp: Annotated[int, category('cp')]
    trestbps: Annotated[float, numeric('trestbps')]
    chol: Annotated[float, numeric('chol')]
    fbs: Annotated[int, category('fbs')]
    restecg: Annotated[int, category('restecg')]
    thalach: Annotated[float, numeric('thalach')]
    exang: Annotated[int, category('exang')]
    oldpeak: Annotated[float, numeric('oldpeak')]
    slope: Annotated[int, category('slope')]
    ca: Annotated[int, category('ca')]
    thal: Annotated[int, category('thal')]


class ModelMetadata(BaseModel):
    name: str = 'Logistic Regression'
    experiment: str = 'Experiment 3'
    preprocessing: str = 'primary_explicit_missing'
    threshold: float = 0.5


class FeatureContribution(BaseModel):
    feature: str
    contribution: float


class Explanation(BaseModel):
    method: str = 'Additive logistic-regression contributions in log-odds units'
    intercept: float
    log_odds: float
    feature_contributions: list[FeatureContribution]
    interpretation: str = ('Contributions sum with the intercept to model log-odds for class 1. '
                           'Positive values increase that model score; these are not medical causes or probabilities.')


class PredictionResponse(BaseModel):
    prediction: Literal[0, 1]
    prediction_label: str
    model_probability: float = Field(ge=0, le=1)
    probability_definition: str = 'Estimated model probability for disease_present=1; not medically validated.'
    model: ModelMetadata
    explanation: Explanation
    missing_features: list[str]
    disclaimer: str


class HealthResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    service: str = 'CardioLens AI'
    model_loaded: bool


class ModelInfoResponse(BaseModel):
    model: str = 'Logistic Regression'
    experiment: str = 'Experiment 3'
    label_definition: str = 'disease_present'
    positive_class: int = 1
    label_mapping: dict[str, str] = {'0': 'UCI-mapped absence', '1': 'UCI-mapped presence'}
    threshold: float = 0.5
    status: str = 'research_prototype'
    features: list[str]
    numeric_supported_ranges: dict[str, list[float]]
    categorical_codes: dict[str, list[int]]
    missing_codes: dict[str, int]
    disclaimer: str
