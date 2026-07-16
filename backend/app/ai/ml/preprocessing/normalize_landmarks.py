"""
normalize_landmarks.py

Responsibilities
----------------
1. Read landmarks.csv.
2. Normalize landmark coordinates.
3. Save normalized_landmarks.csv.

Normalization Strategy
----------------------
Uses DataNormalizer (Wrist-relative normalization).
"""

import os
import pandas as pd

from .data_normalizer import DataNormalizer


class LandmarkDatasetNormalizer:
    """
    Normalize landmark dataset using DataNormalizer.
    """

    def __init__(
        self,
        input_csv="generated/landmarks.csv",
        output_csv="generated/normalized_landmarks.csv"
    ):

        self.input_csv = input_csv
        self.output_csv = output_csv

        self.normalizer = DataNormalizer()

    def normalize(self):

        print("\n==============================")
        print("NORMALIZING LANDMARK DATASET")
        print("==============================\n")

        df = pd.read_csv(self.input_csv)

        feature_columns = list(df.columns[:-1])

        normalized_samples = []

        for _, row in df.iterrows():

            values = row[feature_columns].tolist()

            landmarks = []

            for i in range(0, 63, 3):

                landmarks.append({

                    "x": values[i],

                    "y": values[i + 1],

                    "z": values[i + 2]

                })

            normalized_landmarks = self.normalizer.normalize(
                landmarks
            )

            features = []

            for landmark in normalized_landmarks:

                features.extend([

                    landmark["x"],
                    landmark["y"],
                    landmark["z"]

                ])

            features.append(row["label"])

            normalized_samples.append(features)

        header = feature_columns + ["label"]

        normalized_df = pd.DataFrame(
            normalized_samples,
            columns=header
        )

        os.makedirs(
            os.path.dirname(self.output_csv),
            exist_ok=True
        )

        normalized_df.to_csv(
            self.output_csv,
            index=False
        )

        print("Normalization completed successfully.\n")
        print(f"Input Dataset : {self.input_csv}")
        print(f"Output Dataset: {self.output_csv}")
        print(f"Samples       : {len(normalized_df)}")

        return normalized_df


def main():

    normalizer = LandmarkDatasetNormalizer()

    normalizer.normalize()


if __name__ == "__main__":
    main()