"""
feature_validator.py

Validates extracted hand landmark data
before model prediction.
"""


class FeatureValidator:


    REQUIRED_LANDMARKS = 21


    def __init__(self):
        pass



    def validate(self, landmarks):
        """
        Validate landmark data.

        Args:
            landmarks (list)

        Returns:
            bool
        """


        # Check if landmarks exist

        if landmarks is None:

            return False



        # Check landmark count

        if len(landmarks) != self.REQUIRED_LANDMARKS:

            return False



        # Check every landmark

        for landmark in landmarks:


            if not isinstance(
                landmark,
                dict
            ):

                return False



            required_keys = [
                "x",
                "y",
                "z"
            ]


            for key in required_keys:


                if key not in landmark:

                    return False



                if not isinstance(
                    landmark[key],
                    (int, float)
                ):

                    return False



        return True