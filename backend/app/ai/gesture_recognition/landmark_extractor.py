"""
landmark_extractor.py

Extracts hand landmark coordinates from MediaPipe results.

Responsibilities:
- Extract all 21 landmarks
- Store x, y, z coordinates
- Return structured data
"""

class LandmarkExtractor:
    def __init__(self):
        """
        Initialize Landmark Extractor.
        """
        pass

    def extract(self, results):
        """
        Extract landmark coordinates from MediaPipe results.

        Args:
            results: MediaPipe Hands results object

        Returns:
            list: List of detected hands and their landmarks.
        """

        extracted_data = []

        if not results.multi_hand_landmarks:
            return extracted_data

        for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks, start=1):

            hand_data = {
                "hand": hand_index,
                "landmarks": []
            }

            for landmark_id, landmark in enumerate(hand_landmarks.landmark):

                landmark_data = {
                    "id": landmark_id,
                    "x": round(landmark.x, 6),
                    "y": round(landmark.y, 6),
                    "z": round(landmark.z, 6)
                }

                hand_data["landmarks"].append(landmark_data)

            extracted_data.append(hand_data)

        return extracted_data

    def print_landmarks(self, landmark_data):
        """
        Print landmark coordinates in a structured format.

        Args:
            landmark_data (list)
        """

        if not landmark_data:
            print("\nNo Hand Detected\n")
            return

        for hand in landmark_data:

            print("=" * 50)
            print(f"Hand {hand['hand']}")
            print("=" * 50)

            for landmark in hand["landmarks"]:

                print(
                    f"Landmark {landmark['id']:2d} : "
                    f"x = {landmark['x']:.6f} | "
                    f"y = {landmark['y']:.6f} | "
                    f"z = {landmark['z']:.6f}"
                )

            print("\nNEW FRAME")
            print()