"""
prediction.py

FastAPI endpoint for SignSync AI Engine.
"""

from fastapi import APIRouter, HTTPException

from app.services.gesture_service import (
    GestureService
)

router = APIRouter()

gesture_service = GestureService()


@router.post("/predict")
def predict():
    """
    Prediction endpoint.

    NOTE:
    Image upload and OpenCV decoding
    will be added later.
    """

    try:

        # Placeholder image
        image = None

        result = gesture_service.predict(
            image
        )

        return result.to_dict()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )