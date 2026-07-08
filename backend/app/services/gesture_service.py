"""
gesture_service.py

Gesture prediction service.

Responsibilities:
- Perform gesture prediction
- Return prediction results
- Later integrate the trained AI model
"""

import time

from app.schemas.prediction import PredictionResponse


class GestureService:
    """
    Service responsible for gesture prediction.
    """

    def predict(self) -> PredictionResponse:
        """
        Dummy prediction.

        Returns:
            PredictionResponse
        """

        start_time = time.time()

        # ----------------------------------------
        # Placeholder prediction
        # Replace with AI model in Week 3
        # ----------------------------------------

        prediction = "A"
        confidence = 0.99

        processing_time = time.time() - start_time

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            processing_time=round(processing_time, 6)
        )