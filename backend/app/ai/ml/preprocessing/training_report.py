"""
training_report.py

Responsibilities
----------------
1. Generate training dataset statistics.
2. Export training_report.json.
"""

import json
import os

import pandas as pd


class TrainingReportGenerator:

    def __init__(
        self,
        train_csv="generated/train.csv",
        validation_csv="generated/validation.csv",
        test_csv="generated/test.csv",
        dataset_report="generated/dataset_report.json",
        output_report="generated/training_report.json"
    ):

        self.train_csv = train_csv
        self.validation_csv = validation_csv
        self.test_csv = test_csv
        self.dataset_report = dataset_report
        self.output_report = output_report

    def generate(self):

        print("\n==============================")
        print("GENERATING TRAINING REPORT")
        print("==============================\n")

        train_df = pd.read_csv(self.train_csv)
        validation_df = pd.read_csv(self.validation_csv)
        test_df = pd.read_csv(self.test_csv)

        total_df = pd.concat(
            [train_df, validation_df, test_df],
            ignore_index=True
        )

        with open(self.dataset_report, "r") as file:
            preprocessing_report = json.load(file)
        
        report = {

            "total_samples": len(total_df),

            "gesture_classes": int(
                total_df["label"].nunique()
            ),

            "number_of_features": len(total_df.columns) - 1,

            "training_samples": len(train_df),

            "validation_samples": len(validation_df),

            "testing_samples": len(test_df),

            "failed_landmark_extractions":
              preprocessing_report[
               "failed_detections"
                 ],

            "samples_per_class":
                total_df["label"]
                .value_counts()
                .sort_index()
                .to_dict()

        }

        os.makedirs(
            os.path.dirname(self.output_report),
            exist_ok=True
        )

        with open(
            self.output_report,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        print(json.dumps(report, indent=4))

        print("\nTraining report generated successfully.")

        return report


def main():

    generator = TrainingReportGenerator()

    generator.generate()


if __name__ == "__main__":
    main()