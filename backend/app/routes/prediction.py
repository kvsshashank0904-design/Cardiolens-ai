from fastapi import APIRouter, Request, HTTPException
from ..schemas import PredictionRequest, PredictionResponse

router = APIRouter()

@router.post('/predict', response_model=PredictionResponse)
def predict(payload: PredictionRequest, request: Request):
    service = getattr(request.app.state,'model_service',None)
    if service is None:
        raise HTTPException(status_code=503, detail='Model unavailable.')
    return service.predict(payload)
