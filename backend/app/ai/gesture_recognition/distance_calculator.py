"""
distance_calculator.py

Calculates the Euclidean distance between
Thumb Tip (Landmark 4) and
Index Finger Tip (Landmark 8).
"""

import math


class DistanceCalculator:
    def __init__(self):
        """
        Initialize Distance Calculator.
        """
        self.thumb_tip = 4
        self.index_tip = 8

    def calculate(self, landmark_data):
        """
        Calculate the Euclidean distance between
        Landmark 4 and Landmark 8.

        Args:
            landmark_data (list):
                Output from LandmarkExtractor.extract()

        Returns:
            float | None
        """

        if not landmark_data:
            return None

        try:
            # Use first detected hand
            hand = landmark_data[0]

            thumb = hand["landmarks"][self.thumb_tip]
            index = hand["landmarks"][self.index_tip]

            x1, y1, z1 = thumb["x"], thumb["y"], thumb["z"]
            x2, y2, z2 = index["x"], index["y"], index["z"]

            distance = math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2 +
                (z2 - z1) ** 2
            )

            return round(distance, 6)

        except (IndexError, KeyError):
            return None

    def print_distance(self, distance):
        """
        Print the distance.

        Args:
            distance (float | None)
        """

        if distance is None:
            print("Distance: N/A")
        else:
            print(f"Thumb Tip (4) ↔ Index Tip (8) Distance: {distance:.6f}")