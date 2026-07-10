from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.prediction import router as prediction_router
from app.api.lesson import router as lesson_router
from app.api.practice import router as practice_router
from app.api.preprocess import router as preprocess_router
app = FastAPI()

app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(lesson_router)
app.include_router(practice_router)
app.include_router(preprocess_router)