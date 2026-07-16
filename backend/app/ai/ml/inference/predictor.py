"""
predictor.py

Prediction module for SignSync AI Engine.

Responsibilities
----------------
1. Accept a trained ML model.
2. Predict the gesture.
3. Predict class probabilities.
4. Return prediction and confidence scores.

Used by:
    SignLanguageEngine
"""

import numpy as np


class Predictor:
    """
    Handles model inference.
    """

    def __init__(self, model):

        self.model = model

    # ---------------------------------------------------------
    # Predict Gesture
    # ---------------------------------------------------------

    def predict(self, features):
        """
        Predict gesture class.

        Args:
            features:
                63-dimensional feature vector

        Returns:
            Predicted gesture label
        """

        prediction = self.model.predict(
            [features]
        )[0]

        return prediction

    # ---------------------------------------------------------
    # Predict Probabilities
    # ---------------------------------------------------------

    def predict_probabilities(self, features):
        """
        Predict probability for each class.

        Args:
            features:
                63-dimensional feature vector

        Returns:
            Probability array
        """

        probabilities = self.model.predict_proba(
            [features]
        )[0]

        return probabilities

    # ---------------------------------------------------------
    # Maximum Confidence
    # ---------------------------------------------------------

    def confidence(self, features):
        """
        Return highest prediction confidence.

        Args:
            features:
                63-dimensional feature vector

        Returns:
            float
        """

        probabilities = self.predict_probabilities(
            features
        )

        return float(np.max(probabilities))