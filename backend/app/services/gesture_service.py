"""
gesture_service.py

Service layer for SignSync AI Engine.

Responsibilities
----------------
1. Initialize the AI Engine.
2. Accept image frames.
3. Return structured prediction results.
"""

from app.ai.engine.sign_engine import (
    SignLanguageEngine
)


class GestureService:
    """
    Service wrapper around the AI Engine.
    """

    def __init__(self):

        self.engine = SignLanguageEngine()

    def predict(self, image):
        """
        Predict gesture from an image.

        Args:
            image:
                OpenCV image/frame.

        Returns:
            PredictionResult
        """

        return self.engine.predict(image)