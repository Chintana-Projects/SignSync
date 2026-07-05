"""
dataset_explorer.py

Analyze an ASL dataset and generate statistics.

Features:
- Total number of gesture classes
- Total number of images
- Images per class
- Largest class
- Smallest class
- Export results to CSV
"""

import os
import csv


class DatasetExplorer:

    def __init__(self, dataset_path):
        """
        Initialize Dataset Explorer.

        Args:
            dataset_path (str): Path to the dataset.
        """
        self.dataset_path = dataset_path

    def analyze(self):

        if not os.path.exists(self.dataset_path):
            print("Dataset path not found!")
            return

        class_counts = {}
        total_images = 0

        # Read all class folders
        for class_name in sorted(os.listdir(self.dataset_path)):

            class_path = os.path.join(self.dataset_path, class_name)

            if os.path.isdir(class_path):

                image_count = len([
                    file for file in os.listdir(class_path)
                    if file.lower().endswith(
                        (".jpg", ".jpeg", ".png", ".bmp")
                    )
                ])

                class_counts[class_name] = image_count
                total_images += image_count

        total_classes = len(class_counts)

        largest_class = max(class_counts, key=class_counts.get)
        smallest_class = min(class_counts, key=class_counts.get)

        # -----------------------------
        # Print Results
        # -----------------------------

        print("\n========== DATASET SUMMARY ==========\n")

        print(f"Total Gesture Classes : {total_classes}")
        print(f"Total Images          : {total_images}")

        print("\nImages Per Class\n")

        for cls, count in class_counts.items():
            print(f"{cls:<12} : {count}")

        print("\nLargest Class")
        print(f"{largest_class} ({class_counts[largest_class]} images)")

        print("\nSmallest Class")
        print(f"{smallest_class} ({class_counts[smallest_class]} images)")

        # -----------------------------
        # Save CSV
        # -----------------------------

        csv_filename = "dataset_summary.csv"

        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(["Class", "Number of Images"])

            for cls, count in class_counts.items():
                writer.writerow([cls, count])

            writer.writerow([])
            writer.writerow(["Total Classes", total_classes])
            writer.writerow(["Total Images", total_images])
            writer.writerow(
                ["Largest Class",
                 f"{largest_class} ({class_counts[largest_class]})"]
            )
            writer.writerow(
                ["Smallest Class",
                 f"{smallest_class} ({class_counts[smallest_class]})"]
            )

        print(f"\nCSV exported successfully: {csv_filename}")


if __name__ == "__main__":

    # Change this path to your dataset
    dataset_path = r"C:\Users\DEll\.vscode\Sign\datasets\ASL_Alphabet_Dataset\asl_alphabet_train"

    explorer = DatasetExplorer(dataset_path)
    explorer.analyze()