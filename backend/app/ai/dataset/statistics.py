"""
statistics.py

Keeps track of dataset statistics.

Responsibilities:
- Count processed images
- Count successful detections
- Count failed detections
- Count samples per class
- Store skipped image names
"""


class DatasetStatistics:
    def __init__(self):
        """
        Initialize dataset statistics.
        """

        self.total_images = 0
        self.successful = 0
        self.failed = 0

        self.samples_per_class = {}

        self.skipped_images = []

    def image_processed(self):
        """
        Increment total processed images.
        """

        self.total_images += 1

    def successful_detection(self, class_name):
        """
        Record a successful landmark extraction.

        Args:
            class_name (str)
        """

        self.successful += 1

        if class_name not in self.samples_per_class:
            self.samples_per_class[class_name] = 0

        self.samples_per_class[class_name] += 1

    def failed_detection(self, image_name):
        """
        Record a failed landmark extraction.

        Args:
            image_name (str)
        """

        self.failed += 1
        self.skipped_images.append(image_name)

    def total_classes(self):
        """
        Return total gesture classes.
        """

        return len(self.samples_per_class)

    def largest_class(self):
        """
        Return largest class.
        """

        if not self.samples_per_class:
            return None

        return max(
            self.samples_per_class,
            key=self.samples_per_class.get
        )

    def smallest_class(self):
        """
        Return smallest class.
        """

        if not self.samples_per_class:
            return None

        return min(
            self.samples_per_class,
            key=self.samples_per_class.get
        )

    def print_summary(self):
        """
        Print dataset statistics.
        """

        print("\n" + "=" * 50)
        print("DATASET SUMMARY")
        print("=" * 50)

        print(f"Total Images Processed      : {self.total_images}")
        print(f"Successful Extractions      : {self.successful}")
        print(f"Failed Detections           : {self.failed}")
        print(f"Total Gesture Classes       : {self.total_classes()}")

        print("\nSamples Per Class")

        for class_name, count in sorted(self.samples_per_class.items()):
            print(f"{class_name:<15}: {count}")

        if self.samples_per_class:

            largest = self.largest_class()
            smallest = self.smallest_class()

            print("\nLargest Class")
            print(f"{largest} ({self.samples_per_class[largest]} samples)")

            print("\nSmallest Class")
            print(f"{smallest} ({self.samples_per_class[smallest]} samples)")

        print("=" * 50)