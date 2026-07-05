"""
hand_detector.py

MediaPipe Hand Detection Module.

Responsibilities:
- Detect hands
- Draw landmarks
- Draw landmark connections
- Return detection results
"""

import cv2
import mediapipe as mp


class HandDetector:
    def __init__(
        self,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ):
        """
        Initialize MediaPipe Hands.
        """

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_styles = mp.solutions.drawing_styles

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process(self, frame):
        """
        Detect hands in a frame.

        Args:
            frame (numpy.ndarray)

        Returns:
            processed_frame
            results
        """

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_styles.get_default_hand_landmarks_style(),
                    self.mp_styles.get_default_hand_connections_style()
                )

        return frame, results

    def get_hand_count(self, results):
        """
        Return number of detected hands.
        """

        if results.multi_hand_landmarks:
            return len(results.multi_hand_landmarks)

        return 0

    def close(self):
        """
        Release MediaPipe resources.
        """
        self.hands.close()