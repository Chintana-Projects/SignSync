"""
fps.py

FPS (Frames Per Second) Calculator.

Responsibilities:
- Calculate real-time FPS
- Return the current FPS value
"""

import time


class FPSCounter:
    def __init__(self):
        """
        Initialize FPS counter.
        """
        self.previous_time = time.time()
        self.current_time = time.time()
        self.fps = 0.0

    def update(self):
        """
        Update and return the current FPS.

        Returns:
            float: Current FPS rounded to 2 decimal places.
        """
        self.current_time = time.time()

        time_difference = self.current_time - self.previous_time

        if time_difference > 0:
            self.fps = 1 / time_difference

        self.previous_time = self.current_time

        return round(self.fps, 2)

    def get_fps(self):
        """
        Return the latest FPS value.

        Returns:
            float
        """
        return round(self.fps, 2)

    def reset(self):
        """
        Reset the FPS counter.
        """
        self.previous_time = time.time()
        self.current_time = self.previous_time
        self.fps = 0.0