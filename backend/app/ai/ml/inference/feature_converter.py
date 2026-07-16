"""
feature_converter.py

Converts normalized hand landmarks
into ML model feature vector.
"""


class FeatureConverter:


    def __init__(self):
        pass



    def convert(self, landmarks):
        """
        Convert 21 landmarks into
        63-dimensional feature vector.

        Args:
            landmarks (list)

        Returns:
            list
        """


        if not landmarks:

            return None



        features = []


        for landmark in landmarks:


            features.append(
                landmark["x"]
            )

            features.append(
                landmark["y"]
            )

            features.append(
                landmark["z"]
            )



        return features