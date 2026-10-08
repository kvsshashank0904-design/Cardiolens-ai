from fastapi import APIRouter, Request
from ..config import CONTRACT, FEATURES, DISCLAIMER
from ..schemas import HealthResponse, ModelInfoResponse

router = APIRouter()

@router.get('/health', response_model=HealthResponse)
def health(request: Request):
    return HealthResponse(model_loaded=getattr(request.app.state,'model_service',None) is not None)

@router.get('/model-info', response_model=ModelInfoResponse)
def model_info():
    return ModelInfoResponse(features=list(FEATURES),
        numeric_supported_ranges=CONTRACT['numeric_supported_ranges'], categorical_codes=CONTRACT['categorical_codes'],
        missing_codes=CONTRACT['missing_codes'], disclaimer=DISCLAIMER)
