"""
preprocessing_service.py

Dataset Preprocessing Service

Responsibilities
----------------
1. Start preprocessing.
2. Build landmark dataset.
3. Generate validation report.
4. Return preprocessing summary.
"""

from backend.app.ai.ml.preprocessing.dataset_builder import DatasetBuilder
from backend.app.ai.ml.preprocessing.validator import DatasetValidator


class PreprocessingService:
    """
    Service responsible for dataset preprocessing.
    """

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path

    def preprocess(self):
        """
        Execute the preprocessing pipeline.

        Returns:
            dict
        """

        # -----------------------------
        # Build Dataset
        # -----------------------------

        builder = DatasetBuilder(
            dataset_path=self.dataset_path
        )

        samples = builder.build()

        # -----------------------------
        # Validate Dataset
        # -----------------------------

        validator = DatasetValidator()

        for sample in samples:

            validator.image_processed()

            validator.successful_detection()

        report = validator.generate_report()

        # -----------------------------
        # Return Summary
        # -----------------------------

        return {

            "success": True,

            "message": "Dataset preprocessing completed.",

            "data": {

                "images_processed": report["total_images_processed"],

                "successful": report["successful_landmark_detections"],

                "failed": report["failed_landmark_detections"],

                "csv_file": "generated/landmarks.csv"

            }

        }