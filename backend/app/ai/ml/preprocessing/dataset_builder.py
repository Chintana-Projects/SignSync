"""
dataset_builder.py

Dataset Builder

Responsibilities
----------------
1. Call LandmarkExtractor.
2. Build landmarks.csv.
3. Create CSV header.
4. Store all extracted samples.
"""

import csv
import os

from .extract_landmarks import LandmarkExtractor

class DatasetBuilder:
    """
    Builds landmark dataset CSV.
    """

    def __init__(
        self,
        dataset_path,
        output_csv="generated/landmarks.csv"
    ):

        self.dataset_path = dataset_path
        self.output_csv = output_csv

    def build(self):

        print("\n==============================")
        print("BUILDING LANDMARK DATASET")
        print("==============================\n")

        extractor = LandmarkExtractor(
    dataset_path=self.dataset_path,
    normalize=False
)

        samples = extractor.extract()

        os.makedirs(
            os.path.dirname(self.output_csv),
            exist_ok=True
        )

        header = []

        for i in range(21):

            header.extend([
                f"x{i}",
                f"y{i}",
                f"z{i}"
            ])

        header.append("label")

        with open(
            self.output_csv,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(header)

            for sample in samples:

                row = sample["features"] + [sample["label"]]
                writer.writerow(row)

        print(f"\nDataset saved to: {self.output_csv}")
        print(f"Total Samples: {len(samples)}")

        return samples


def main():

    dataset_path = (
        r"C:\Users\DEll\.vscode\Sign\datasets"
        r"\ASL_Alphabet_Dataset\asl_alphabet_train"
    )

    builder = DatasetBuilder(
        dataset_path=dataset_path
    )

    builder.build()


if __name__ == "__main__":
    main()