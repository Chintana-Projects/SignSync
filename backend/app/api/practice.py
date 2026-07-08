"""
practice.py

Practice API.
"""

from fastapi import APIRouter, HTTPException

from app.schemas.practice import PracticeResponse
from app.services.practice_service import PracticeService

router = APIRouter()

practice_service = PracticeService()


@router.post(
    "/practice/{lesson_id}",
    response_model=PracticeResponse
)
def start_practice(lesson_id: int):
    """
    Start a practice session.
    """

    response = practice_service.start_practice(lesson_id)

    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found."
        )

    return response