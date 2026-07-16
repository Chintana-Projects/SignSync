"""
test_engine.py

Basic test for SignSync AI Engine.
"""

import cv2

from app.ai.engine.sign_engine import SignLanguageEngine


def main():

    engine = SignLanguageEngine()

    image = cv2.imread("sample.jpg")

    if image is None:
        print("Sample image not found.")
        return

    result = engine.predict(image)

    print(result.to_dict())


if __name__ == "__main__":
    main()