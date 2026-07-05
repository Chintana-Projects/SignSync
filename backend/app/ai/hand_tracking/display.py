"""
display.py

Display Module.

Responsibilities:
- Display FPS
- Display hand count
- Display "No Hand Detected"
"""

import cv2


class Display:
    def __init__(self):
        """
        Display configuration.
        """
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.8
        self.font_thickness = 2

        # Colors (BGR)
        self.green = (0, 255, 0)
        self.red = (0, 0, 255)
        self.blue = (255, 0, 0)
        self.white = (255, 255, 255)

    def draw_status(self, frame, fps, hand_count):
        """
        Draw FPS and hand information.

        Args:
            frame: Video frame
            fps: Current FPS
            hand_count: Number of detected hands

        Returns:
            frame
        """

        # FPS
        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 35),
            self.font,
            self.font_scale,
            self.green,
            self.font_thickness
        )

        # Hand count
        if hand_count > 0:
            cv2.putText(
                frame,
                f"Hands Detected: {hand_count}",
                (20, 70),
                self.font,
                self.font_scale,
                self.blue,
                self.font_thickness
            )
        else:
            cv2.putText(
                frame,
                "No Hand Detected",
                (20, 70),
                self.font,
                self.font_scale,
                self.red,
                self.font_thickness
            )

        return frame

    def draw_message(self, frame, message, position=(20, 110)):
        """
        Draw a custom message on the frame.

        Args:
            frame: Video frame
            message: Text to display
            position: (x, y)
        """

        cv2.putText(
            frame,
            message,
            position,
            self.font,
            self.font_scale,
            self.white,
            self.font_thickness
        )

        return frame