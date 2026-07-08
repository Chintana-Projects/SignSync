"""
practice.py

Practice session response schema.
"""

from pydantic import BaseModel

from app.schemas.lesson import Lesson
from app.schemas.prediction import PredictionResponse


class Session(BaseModel):
    session_id: str
    lesson_id: int
    start_time: str
    end_time: str | None
    attempts: int


class PracticeResponse(BaseModel):
    session: Session
    lesson: Lesson
    camera: str
    hand_detection: str
    landmarks: str
    prediction: PredictionResponse
    status: str