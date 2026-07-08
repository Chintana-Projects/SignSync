"""
lesson.py

Pydantic schema for lesson content.

Responsibilities:
- Validate lesson data
- Generate API documentation
"""

from pydantic import BaseModel


class Lesson(BaseModel):
    """
    Represents one learning lesson.
    """

    id: int
    sign: str
    description: str
    meaning: str
    image: str
    difficulty: str