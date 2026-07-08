"""
report_generator.py

Generates reports after dataset extraction.

Responsibilities:
- Save dataset statistics to JSON
- Save skipped image names to TXT
"""

import os
import json


class ReportGenerator:

    def __init__(self, output_directory="generated"):
        """
        Initialize Report Generator.

        Args:
            output_directory (str)
        """

        self.output_directory = output_directory

        os.makedirs(self.output_directory, exist_ok=True)

    def generate_json_report(self, statistics):
        """
        Save dataset statistics into JSON.

        Args:
            statistics (DatasetStatistics)
        """

        report = {

            "total_images_processed": statistics.total_images,

            "successful_extractions": statistics.successful,

            "failed_detections": statistics.failed,

            "number_of_classes": statistics.total_classes(),

            "samples_per_class": statistics.samples_per_class

        }

        report_path = os.path.join(
            self.output_directory,
            "dataset_report.json"
        )

        with open(report_path, "w", encoding="utf-8") as file:

            json.dump(report, file, indent=4)

        print(f"\nJSON Report Saved:")
        print(report_path)

    def save_skipped_images(self, statistics):
        """
        Save skipped image filenames.

        Args:
            statistics (DatasetStatistics)
        """

        skipped_path = os.path.join(
            self.output_directory,
            "skipped_images.txt"
        )

        with open(skipped_path, "w", encoding="utf-8") as file:

            if not statistics.skipped_images:

                file.write("No skipped images.\n")

            else:

                for image in statistics.skipped_images:
                    file.write(image + "\n")

        print("\nSkipped Images Log Saved:")
        print(skipped_path)