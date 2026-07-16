"""
model_loader.py

Generic Model Loader

Responsibilities
----------------
1. Load any trained ML model.
2. Support Random Forest, Decision Tree and SVM.
"""

import joblib

from ..training.model_config import MODEL_PATHS


class ModelLoader:
    """
    Generic model loader.
    """

    def __init__(self):

        self.model = None

    def load(self, algorithm):
        """
        Load a trained model.

        Args:
            algorithm (str):
                RandomForest
                DecisionTree
                SVM

        Returns:
            Trained model
        """

        if algorithm not in MODEL_PATHS:

            raise ValueError(
                f"Unsupported Algorithm : {algorithm}"
            )

        model_path = MODEL_PATHS[algorithm]

        self.model = joblib.load(model_path)

        print("\n==============================")
        print("MODEL LOADED")
        print("==============================")
        print(f"Algorithm : {algorithm}")
        print(f"Location  : {model_path}")
        print("==============================")

        return self.model


def main():

    loader = ModelLoader()

    # Example
    # loader.load("RandomForest")


if __name__ == "__main__":
    main()