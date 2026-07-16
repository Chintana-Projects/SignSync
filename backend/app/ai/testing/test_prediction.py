import cv2

from app.ai.engine.sign_engine import SignLanguageEngine


def main():

    engine = SignLanguageEngine()

    image = cv2.imread("C:\\Users\\DEll\\.vscode\\Sign\\datasets\\ASL_Alphabet_Dataset\\asl_alphabet_test\\I_test.jpg")

    if image is None:
        print("Image not found.")
        return

    result = engine.predict(image)

    print("\nPrediction Result")
    print("-----------------")
    print(result.to_dict())


if __name__ == "__main__":
    main()