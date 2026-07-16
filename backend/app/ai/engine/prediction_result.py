"""
prediction_result.py

Defines the standard output format
of the SignSync AI Engine.
"""


class PredictionResult:


    def __init__(
        self,
        gesture,
        confidence,
        model_version,
        inference_time_ms,
        status="success"
    ):

        self.gesture = gesture

        self.confidence = confidence

        self.model_version = model_version

        self.inference_time_ms = inference_time_ms

        self.status = status



    def to_dict(self):
        """
        Convert prediction result
        into JSON-compatible format.
        """

        return {

            "status": self.status,

            "gesture": self.gesture,

            "confidence": round(
                float(self.confidence),
                4
            ),

            "model_version":
                self.model_version,

            "inference_time_ms":
                round(
                    float(self.inference_time_ms),
                    4
                )

        }