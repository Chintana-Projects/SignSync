"""
hand_detector.py

Handles MediaPipe hand detection.

Input:
    Image frame

Output:
    21 hand landmarks
    or None if no hand detected
"""


import mediapipe as mp


class HandDetector:


    def __init__(self):

        self.mp_hands = mp.solutions.hands


        self.hands = self.mp_hands.Hands(

            static_image_mode=False,

            max_num_hands=1,

            min_detection_confidence=0.7,

            min_tracking_confidence=0.7

        )


    def detect(self, image):
        """
        Detect hand landmarks.

        Args:
            image:
                OpenCV image

        Returns:
            list of landmarks
            or None
        """


        if image is None:

            return None



        # Convert BGR → RGB

        rgb_image = image[:, :, ::-1]


        results = self.hands.process(
            rgb_image
        )


        # No hand detected

        if not results.multi_hand_landmarks:

            return None



        hand = results.multi_hand_landmarks[0]


        landmarks = []


        for point in hand.landmark:


            landmarks.append({

                "x": point.x,

                "y": point.y,

                "z": point.z

            })


        return landmarks