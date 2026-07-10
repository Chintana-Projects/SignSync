"""
validator.py

Dataset Validator

Responsibilities
----------------
1. Validate extracted dataset.
2. Generate preprocessing statistics.
3. Export dataset_report.json.
"""

import json
import os


class DatasetValidator:
    """
    Generates dataset validation statistics.
    """

    def __init__(self):

        self.total_images = 0
        self.successful = 0
        self.failed = 0
        self.corrupted = 0

    def image_processed(self):
        self.total_images += 1

    def successful_detection(self):
        self.successful += 1

    def failed_detection(self):
        self.failed += 1

    def corrupted_image(self):
        self.corrupted += 1

    def generate_report(
        self,
        output_path="generated/dataset_report.json"
    ):

        success_percentage = 0.0

        if self.total_images > 0:

            success_percentage = round(
                (self.successful / self.total_images) * 100,
                2
            )

        report = {

            "total_images_processed": self.total_images,

            "successful_landmark_detections": self.successful,

            "failed_landmark_detections": self.failed,

            "corrupted_images": self.corrupted,

            "success_percentage": success_percentage

        }

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        print("\n==============================")
        print("DATASET VALIDATION REPORT")
        print("==============================")
        print(json.dumps(report, indent=4))
        print("==============================")

        return report