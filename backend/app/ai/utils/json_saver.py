"""
json_saver.py

Save landmark data to JSON files.

Responsibilities:
- Save landmark data
- Add timestamp
- Auto-generate filenames
"""

import json

from app.ai.utils.helpers import (
    get_timestamp,
    get_next_capture_filename,
    ensure_directory_exists
)


class JSONSaver:
    def __init__(self, capture_directory="captures"):
        """
        Initialize JSON Saver.

        Args:
            capture_directory (str)
        """
        self.capture_directory = capture_directory
        ensure_directory_exists(self.capture_directory)

    def save(self, landmark_data):
        print("SAVE FUNCTION CALLED")
        """
        Save landmark data to a JSON file.

        Args:
            landmark_data (list)

        Returns:
            str | None
                Path of saved JSON file.
        """
         
        if not landmark_data:
            print("No hand detected. Nothing to save.")
            return None

        data = {
            "timestamp": get_timestamp(),
            "number_of_hands": len(landmark_data),
            "hands": landmark_data
        }

        filename = get_next_capture_filename(self.capture_directory)
        import os
        print("Current Working Directory:", os.getcwd())
        print("Saving to:", os.path.abspath(filename))
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"\nLandmarks saved successfully!")
        print(f"File: {filename}\n")

        return filename