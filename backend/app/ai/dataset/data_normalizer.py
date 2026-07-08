"""
data_normalizer.py

Normalizes landmark coordinates.

Current Strategy:
- Translation normalization
- Wrist (Landmark 0) becomes the origin.
"""


class DataNormalizer:

    def __init__(self):
        """
        Initialize Data Normalizer.
        """
        pass

    def normalize(self, landmarks):
        """
        Normalize landmarks using Landmark 0 (Wrist).

        Args:
            landmarks (list)

        Returns:
            list
        """

        if not landmarks:
            return landmarks

        wrist = landmarks[0]

        wrist_x = wrist["x"]
        wrist_y = wrist["y"]
        wrist_z = wrist["z"]

        normalized = []

        for landmark in landmarks:

            normalized.append({

                "x": round(landmark["x"] - wrist_x, 6),

                "y": round(landmark["y"] - wrist_y, 6),

                "z": round(landmark["z"] - wrist_z, 6)

            })

        return normalized