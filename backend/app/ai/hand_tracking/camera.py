"""
camera.py

Reusable webcam module.

Responsibilities:
- Open the webcam
- Read video frames
- Release the webcam
"""

import cv2


class Camera:
    def __init__(self, camera_index=0, width=1280, height=720):
        """
        Initialize camera settings.

        Args:
            camera_index (int): Webcam index (default = 0)
            width (int): Frame width
            height (int): Frame height
        """
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.cap = None

    def start(self):
        """
        Open the webcam.

        Returns:
            bool: True if successful, False otherwise.
        """
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            return False

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        return True

    def read(self):
        """
        Read a frame from the webcam.

        Returns:
            tuple:
                success (bool)
                frame (numpy.ndarray)
        """
        if self.cap is None:
            return False, None

        success, frame = self.cap.read()

        if not success:
            return False, None

        # Flip horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        return True, frame

    def release(self):
        """
        Release the webcam.
        """
        if self.cap is not None:
            self.cap.release()
            self.cap = None