from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .config import MODEL_PATH
from .model_service import ModelService, InferenceError
from .routes import health, prediction


def create_app(artifact_path: Path = MODEL_PATH) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app):
        # One load per application process, before accepting requests. Failure aborts startup.
        app.state.model_service = ModelService(artifact_path)
        yield
        app.state.model_service = None

    app = FastAPI(title='CardioLens AI', version='1.0.0',
                  description='Frozen Experiment 3 model inference. Research prototype; not a medical diagnosis.',
                  lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:3001",
            "http://127.0.0.1:3001",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError):
        # Do not echo request values (including NaN), exception contexts, or internal paths.
        errors = [{'location':list(e['loc']), 'message':e['msg'], 'type':e['type']} for e in exc.errors()]
        return JSONResponse(status_code=422,content={'detail':errors})

    @app.exception_handler(InferenceError)
    async def inference_error(request: Request, exc: InferenceError):
        return JSONResponse(status_code=500,content={'detail':'Prediction could not be completed.'})

    @app.exception_handler(Exception)
    async def unexpected_error(request: Request, exc: Exception):
        return JSONResponse(status_code=500,content={'detail':'Internal service error.'})

    app.include_router(health.router)
    app.include_router(prediction.router)
    return app


app = create_app()
