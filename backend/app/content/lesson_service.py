"""
lesson_service.py

Learning Content Service.

Responsibilities:
- Store lesson information
- Return all lessons
- Return a lesson by ID
"""


class LessonService:
    """
    Service responsible for managing learning lessons.
    """

    def __init__(self):
        """
        Initialize lesson content.
        """

        self.lessons = [
            {
                "id": 1,
                "sign": "A",
                "description": "Closed fist with thumb resting on the side.",
                "meaning": "Represents the alphabet A.",
                "image": "assets/asl/A.jpg",
                "difficulty": "Beginner"
            },
            {
                "id": 2,
                "sign": "B",
                "description": "Open palm with fingers together and thumb across the palm.",
                "meaning": "Represents the alphabet B.",
                "image": "assets/asl/B.jpg",
                "difficulty": "Beginner"
            },
            {
                "id": 3,
                "sign": "C",
                "description": "Curve your fingers and thumb to form the shape of the letter C.",
                "meaning": "Represents the alphabet C.",
                "image": "assets/asl/C.jpg",
                "difficulty": "Beginner"
            },
            {
                "id": 4,
                "sign": "D",
                "description": "Index finger points upward while the thumb touches the middle finger.",
                "meaning": "Represents the alphabet D.",
                "image": "assets/asl/D.jpg",
                "difficulty": "Beginner"
            },
            {
                "id": 5,
                "sign": "E",
                "description": "Fingers curl down toward the palm with the thumb crossing the fingertips.",
                "meaning": "Represents the alphabet E.",
                "image": "assets/asl/E.jpg",
                "difficulty": "Beginner"
            }
        ]

    def get_all_lessons(self):
        """
        Return all lessons.

        Returns:
            list
        """
        return self.lessons

    def get_lesson_by_id(self, lesson_id):
        """
        Return a lesson by its ID.

        Args:
            lesson_id (int)

        Returns:
            dict | None
        """

        for lesson in self.lessons:
            if lesson["id"] == lesson_id:
                return lesson

        return None