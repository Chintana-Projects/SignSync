"""
lesson.py

Lesson API.

Responsibilities:
- Return all lessons
- Return lesson details
"""

from fastapi import APIRouter, HTTPException

from app.content.lesson_service import LessonService
from app.schemas.lesson import Lesson

router = APIRouter()

lesson_service = LessonService()


@router.get(
    "/lessons",
    response_model=list[Lesson]
)
def get_lessons():
    """
    Return all available lessons.
    """
    return lesson_service.get_all_lessons()


@router.get(
    "/lessons/{lesson_id}",
    response_model=Lesson
)
def get_lesson(lesson_id: int):
    """
    Return lesson details by ID.
    """

    lesson = lesson_service.get_lesson_by_id(lesson_id)

    if lesson is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found."
        )

    return lesson