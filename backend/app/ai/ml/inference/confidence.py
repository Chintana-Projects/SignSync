"""
confidence.py

Confidence evaluation for SignSync AI Engine.

Responsibilities
----------------
1. Calculate prediction confidence.
2. Check prediction confidence.
3. Apply confidence threshold.
4. Decide whether prediction is reliable.
"""


class ConfidenceCalculator:
    """
    Handles confidence calculation and threshold checking.
    """

    def __init__(self, threshold=0.70):

        self.threshold = threshold


    # ---------------------------------------------------------
    # Calculate Confidence
    # ---------------------------------------------------------

    def calculate(self, model, features):
        """
        Calculate prediction confidence.

        Args:
            model:
                Loaded ML model.

            features:
                63-dimensional feature vector.

        Returns:
            Confidence score between 0 and 1.
        """

        probabilities = model.predict_proba(
            [features]
        )

        confidence = max(
            probabilities[0]
        )

        return confidence



    # ---------------------------------------------------------
    # Check Confidence
    # ---------------------------------------------------------

    def is_confident(self, confidence):
        """
        Returns True if confidence is above threshold.
        """

        return confidence >= self.threshold



    # ---------------------------------------------------------
    # Apply Confidence Threshold
    # ---------------------------------------------------------

    def apply_threshold(self, prediction, confidence):
        """
        Apply confidence threshold.

        If confidence is low:
            return Unknown

        Else:
            return predicted gesture
        """

        if self.is_confident(confidence):

            return prediction


        return "Unknown"



    # ---------------------------------------------------------
    # Get Threshold
    # ---------------------------------------------------------

    def get_threshold(self):
        """
        Return current confidence threshold.
        """

        return self.threshold



    # ---------------------------------------------------------
    # Update Threshold
    # ---------------------------------------------------------

    def set_threshold(self, threshold):
        """
        Update confidence threshold.
        """

        self.threshold = threshold