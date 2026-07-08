"""
extract_landmarks.py

Main script for creating a landmark dataset.

Responsibilities
----------------
1. Traverse every image in the ASL dataset.
2. Detect hands using MediaPipe.
3. Extract all 21 landmarks.
4. (Optional) Normalize landmarks.
5. Flatten landmarks into 63 features.
6. Append the class label.
7. Save everything into a CSV file.
8. Skip invalid samples.
9. Generate statistics and reports.
"""

import os
import cv2
import mediapipe as mp

from csv_writer import CSVWriter
from statistics import DatasetStatistics
from report_generator import ReportGenerator
from data_normalizer import DataNormalizer


class LandmarkDatasetExtractor:

    def __init__(
        self,
        dataset_path,
        output_csv="generated/landmark_dataset.csv",
        normalize=True
    ):

        self.dataset_path = dataset_path

        self.writer = CSVWriter(output_csv)

        self.statistics = DatasetStatistics()

        self.report_generator = ReportGenerator()

        self.normalize = normalize

        self.normalizer = DataNormalizer()

        # -----------------------------
        # MediaPipe Hands
        # -----------------------------

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(

            static_image_mode=True,

            max_num_hands=1,

            min_detection_confidence=0.5

        )

    def extract_dataset(self):

        print("\n===============================")
        print("LANDMARK EXTRACTION STARTED")
        print("===============================\n")

        class_folders = sorted(os.listdir(self.dataset_path))

        for class_name in class_folders:

            class_path = os.path.join(
                self.dataset_path,
                class_name
            )

            if not os.path.isdir(class_path):
                continue

            print(f"Processing Class: {class_name}")

            image_files = sorted(os.listdir(class_path))

            for image_name in image_files:

                image_path = os.path.join(
                    class_path,
                    image_name
                )

                self.statistics.image_processed()

                image = cv2.imread(image_path)

                if image is None:

                    self.statistics.failed_detection(image_path)

                    continue

                rgb = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                )

                results = self.hands.process(rgb)

                if not results.multi_hand_landmarks:

                    self.statistics.failed_detection(image_path)

                    continue

                hand = results.multi_hand_landmarks[0]

                landmarks = []

                for landmark in hand.landmark:

                    landmarks.append({

                        "x": round(landmark.x, 6),

                        "y": round(landmark.y, 6),

                        "z": round(landmark.z, 6)

                    })

                # --------------------------
                # Optional Normalization
                # --------------------------

                if self.normalize:

                    landmarks = self.normalizer.normalize(
                        landmarks
                    )

                # --------------------------
                # Save CSV Row
                # --------------------------

                self.writer.write_sample(

                    landmarks,

                    class_name

                )

                self.statistics.successful_detection(
                    class_name
                )
                        # -----------------------------
        # Finished Processing Dataset
        # -----------------------------

        self.hands.close()

        print("\n")
        self.statistics.print_summary()

        self.report_generator.generate_json_report(
            self.statistics
        )

        self.report_generator.save_skipped_images(
            self.statistics
        )

        print("\n")
        print("=" * 60)
        print("LANDMARK DATASET CREATED SUCCESSFULLY")
        print("=" * 60)

        print(f"CSV File : {self.writer.get_output_path()}")

        print("Reports  : generated/")
        print("=" * 60)


def main():

    # -------------------------------------------------
    # CHANGE THIS PATH TO YOUR ASL DATASET LOCATION
    # -------------------------------------------------

    dataset_path = r"C:\Users\DEll\.vscode\Sign\datasets\ASL_Alphabet_Dataset\asl_alphabet_train"

    extractor = LandmarkDatasetExtractor(

        dataset_path=dataset_path,

        output_csv="generated/landmark_dataset.csv",

        normalize=True

    )

    extractor.extract_dataset()


if __name__ == "__main__":
    main()