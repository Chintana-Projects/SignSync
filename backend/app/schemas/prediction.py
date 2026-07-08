"""
prediction.py

Pydantic response schema for gesture prediction.

Responsibilities:
- Define API response format
- Validate response data
- Generate API documentation
"""

from pydantic import BaseModel


class PredictionResponse(BaseModel):
    """
    Response returned by the prediction API.
    """

    prediction: str
    confidence: float
    processing_time: float