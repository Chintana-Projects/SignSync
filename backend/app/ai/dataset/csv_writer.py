"""
csv_writer.py

Writes extracted hand landmark data to a CSV file.

Responsibilities:
- Create output directory if needed
- Create CSV file with header
- Append one sample at a time
"""

import os
import csv


class CSVWriter:
    def __init__(self, output_path):
        """
        Initialize CSV Writer.

        Args:
            output_path (str): Path of the output CSV file.
        """

        self.output_path = output_path

        # Create output folder if it doesn't exist
        output_folder = os.path.dirname(self.output_path)

        if output_folder:
            os.makedirs(output_folder, exist_ok=True)

        # Create CSV and write header only once
        if not os.path.exists(self.output_path):
            self._write_header()

    def _write_header(self):
        """
        Write CSV header.

        Header Format:
        x0,y0,z0,x1,y1,z1,...,x20,y20,z20,label
        """

        header = []

        # Create x,y,z columns for all 21 landmarks
        for i in range(21):
            header.append(f"x{i}")
            header.append(f"y{i}")
            header.append(f"z{i}")

        header.append("label")

        with open(self.output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)

    def write_sample(self, landmarks, label):
        """
        Write one landmark sample to CSV.

        Args:
            landmarks (list): List of 21 landmark dictionaries.
            label (str): Gesture class label.
        """

        # Ensure exactly 21 landmarks
        if len(landmarks) != 21:
            print("Skipped sample: Expected 21 landmarks.")
            return

        row = []

        for landmark in landmarks:
            row.extend([
                landmark["x"],
                landmark["y"],
                landmark["z"]
            ])

        row.append(label)

        with open(self.output_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        # Force data to be written immediately
        

    def get_output_path(self):
        """
        Return output CSV path.

        Returns:
            str
        """
        return self.output_path