"""
extract_landmarks.py

Landmark Extraction Pipeline

Responsibilities
----------------
1. Traverse every image in the ASL dataset.
2. Detect hands using MediaPipe.
3. Extract all 21 landmarks.
4. Optionally normalize landmarks.
5. Flatten landmarks into 63 numerical values.
6. Return extracted samples.

Note:
This module DOES NOT:
- Write CSV files
- Generate reports
- Validate datasets

Those responsibilities belong to:
- dataset_builder.py
- validator.py
"""

import os
import cv2
import mediapipe as mp

from .data_normalizer import DataNormalizer
class LandmarkExtractor:
    """
    Extracts hand landmarks from an ASL dataset.
    """

    def __init__(
        self,
        dataset_path,
        normalize=True
    ):
        self.dataset_path = dataset_path

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

    def extract(self):
        """
        Traverse the dataset and extract landmarks.

        Returns:
            list[dict]
        """

        dataset = []

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

                image = cv2.imread(image_path)

                if image is None:
                    continue

                rgb = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                )

                results = self.hands.process(rgb)

                if not results.multi_hand_landmarks:
                    continue

                hand = results.multi_hand_landmarks[0]

                landmarks = []

                for landmark in hand.landmark:

                    landmarks.append({
                        "x": round(landmark.x, 6),
                        "y": round(landmark.y, 6),
                        "z": round(landmark.z, 6)
                    })

                # -----------------------------
                # Optional Normalization
                # -----------------------------

                if self.normalize:

                    landmarks = self.normalizer.normalize(
                        landmarks
                    )

                # -----------------------------
                # Flatten into 63 values
                # -----------------------------

                features = []

                for landmark in landmarks:

                    features.extend([
                        landmark["x"],
                        landmark["y"],
                        landmark["z"]
                    ])

                dataset.append({

                    "label": class_name,

                    "features": features,

                    "image": image_path

                })

        self.hands.close()

        return dataset


def main():

    dataset_path = (
        r"C:\Users\DEll\.vscode\Sign\datasets"
        r"\ASL_Alphabet_Dataset\asl_alphabet_train"
    )

    extractor = LandmarkExtractor(

        dataset_path=dataset_path,

        normalize=True

    )

    dataset = extractor.extract()

    print("\n======================================")
    print("LANDMARK EXTRACTION COMPLETED")
    print("======================================")
    print(f"Extracted Samples : {len(dataset)}")
    print("======================================")


if __name__ == "__main__":
    main()