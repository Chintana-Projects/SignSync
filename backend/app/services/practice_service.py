"""
practice_service.py

Practice Session Workflow.

Responsibilities:
- Manage lesson practice flow
- Simulate AI assessment workflow
- Return placeholder response
"""

from app.content.lesson_service import LessonService
from app.services.gesture_service import GestureService
from app.services.session_service import SessionService

class PracticeService:
    """
    Service responsible for the practice workflow.
    """

    def __init__(self):
        self.lesson_service = LessonService()
        self.gesture_service = GestureService()
        self.session_service = SessionService()

    def start_practice(self, lesson_id: int):
        """
        Start a practice session.

        Workflow:
            Lesson Selected
                    ↓
            Lesson Loaded
                    ↓
            Camera Ready
                    ↓
            Hand Detection
                    ↓
            Landmark Extraction
                    ↓
            Placeholder Prediction
                    ↓
            Session Complete
        """

        lesson = self.lesson_service.get_lesson_by_id(lesson_id)
        session = self.session_service.start_session(lesson_id)
        if lesson is None:
            return None

        workflow = {
            "session": session,
            "lesson": lesson,
            "camera": "Ready",
            "hand_detection": "Waiting",
            "landmarks": "Not Extracted",
            "prediction": self.gesture_service.predict(),
            "status": "Practice Completed"
            
        }

        return workflow