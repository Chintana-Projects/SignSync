from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.prediction import router as prediction_router

app = FastAPI(
    title="SignSync Backend",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(prediction_router)