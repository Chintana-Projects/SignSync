"""
prediction.py

Prediction API.

Responsibilities:
- Expose gesture prediction endpoint
- Delegate prediction to GestureService
"""

from fastapi import APIRouter

from app.schemas.prediction import PredictionResponse
from app.services.gesture_service import GestureService

router = APIRouter()

gesture_service = GestureService()


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict():
    """
    Predict a hand gesture.

    Returns:
        PredictionResponse
    """
    return gesture_service.predict()