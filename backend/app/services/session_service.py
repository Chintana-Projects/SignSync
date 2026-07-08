"""
session_service.py

Practice Session Manager.

Responsibilities:
- Create practice sessions
- End practice sessions
- Store session data in JSON
"""

import json
import os
import uuid
from datetime import datetime


class SessionService:
    """
    Service responsible for managing practice sessions.
    """

    def __init__(self):

        self.session_file = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "sessions.json"
        )

    def _load_sessions(self):
        """
        Load all sessions.
        """

        if not os.path.exists(self.session_file):
            return []

        with open(self.session_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save_sessions(self, sessions):
        """
        Save all sessions.
        """

        with open(self.session_file, "w", encoding="utf-8") as file:
            json.dump(sessions, file, indent=4)

    def start_session(self, lesson_id: int):
        """
        Create a new practice session.
        """

        sessions = self._load_sessions()

        session = {
            "session_id": str(uuid.uuid4()),
            "lesson_id": lesson_id,
            "start_time": datetime.now().isoformat(),
            "end_time": None,
            "attempts": 0
        }

        sessions.append(session)

        self._save_sessions(sessions)

        return session

    def end_session(self, session_id: str):
        """
        End a practice session.
        """

        sessions = self._load_sessions()

        for session in sessions:

            if session["session_id"] == session_id:

                session["end_time"] = datetime.now().isoformat()

                self._save_sessions(sessions)

                return session

        return None

    def increment_attempt(self, session_id: str):
        """
        Increase attempt count.
        """

        sessions = self._load_sessions()

        for session in sessions:

            if session["session_id"] == session_id:

                session["attempts"] += 1

                self._save_sessions(sessions)

                return session

        return None