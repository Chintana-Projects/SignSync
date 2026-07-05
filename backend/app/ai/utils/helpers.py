"""
helpers.py

Common utility functions used across the project.

Responsibilities:
- Generate timestamps
- Create sequential filenames
- Create directories if they don't exist
"""

import os
from datetime import datetime


def get_timestamp():
    """
    Return the current timestamp.

    Returns:
        str: Timestamp in YYYY-MM-DD HH:MM:SS format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ensure_directory_exists(directory_path):
    """
    Create the directory if it doesn't exist.

    Args:
        directory_path (str)
    """
    os.makedirs(directory_path, exist_ok=True)


def get_next_capture_filename(directory, prefix="capture_", extension=".json"):
    """
    Generate the next available capture filename.

    Example:
        capture_001.json
        capture_002.json
        capture_003.json

    Args:
        directory (str)
        prefix (str)
        extension (str)

    Returns:
        str: Full path of the next filename.
    """

    ensure_directory_exists(directory)

    existing_files = [
        file for file in os.listdir(directory)
        if file.startswith(prefix) and file.endswith(extension)
    ]

    if not existing_files:
        next_number = 1
    else:
        numbers = []

        for file in existing_files:
            try:
                number = int(
                    file.replace(prefix, "").replace(extension, "")
                )
                numbers.append(number)
            except ValueError:
                continue

        next_number = max(numbers) + 1 if numbers else 1

    filename = f"{prefix}{next_number:03d}{extension}"

    return os.path.join(directory, filename)


def project_root():
    """
    Return the project root directory.

    Returns:
        str
    """
    return os.getcwd()