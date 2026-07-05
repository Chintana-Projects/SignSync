"""
run.py

Main application for AI Hand Tracking.

Features:
- Webcam
- MediaPipe Hand Tracking
- FPS Counter
- Hand Count
- Landmark Extraction
- JSON Saving (Press S)
- Euclidean Distance (Bonus)
- Quit (Press Q)
"""

import cv2

from app.ai.hand_tracking.camera import Camera
from app.ai.hand_tracking.hand_detector import HandDetector
from app.ai.hand_tracking.fps import FPSCounter
from app.ai.hand_tracking.display import Display

from app.ai.gesture_recognition.landmark_extractor import LandmarkExtractor
from app.ai.gesture_recognition.distance_calculator import DistanceCalculator

from app.ai.utils.json_saver import JSONSaver


def main():

    # ----------------------------
    # Initialize Modules
    # ----------------------------

    camera = Camera()
    detector = HandDetector()
    fps_counter = FPSCounter()
    display = Display()
    extractor = LandmarkExtractor()
    distance_calculator = DistanceCalculator()
    json_saver = JSONSaver()

    # ----------------------------
    # Open Camera
    # ----------------------------

    if not camera.start():
        print("Unable to open webcam.")
        return

    print("\n===================================")
    print(" AI Hand Tracking Started")
    print("===================================")
    print("Press 'S' to Save Landmarks")
    print("Press 'Q' to Quit")
    print("===================================\n")

    while True:

        success, frame = camera.read()

        if not success:
            print("Failed to read frame.")
            break

        # ---------------------------------
        # Detect Hands
        # ---------------------------------

        frame, results = detector.process(frame)

        hand_count = detector.get_hand_count(results)

        # ---------------------------------
        # Extract Landmarks
        # ---------------------------------

        landmark_data = extractor.extract(results)

        # ---------------------------------
        # Calculate Distance
        # ---------------------------------

        distance = distance_calculator.calculate(landmark_data)

        # ---------------------------------
        # Calculate FPS
        # ---------------------------------

        fps = fps_counter.update()

        # ---------------------------------
        # Draw Status
        # ---------------------------------

        display.draw_status(frame, fps, hand_count)

        # ---------------------------------
        # Draw Distance
        # ---------------------------------

        if distance is not None:

            display.draw_message(
                frame,
                f"Thumb-Index Distance: {distance:.6f}",
                position=(20, 110)
            )

        else:

            display.draw_message(
                frame,
                "Thumb-Index Distance: N/A",
                position=(20, 110)
            )

        # ---------------------------------
        # Display Webcam
        # ---------------------------------

        cv2.imshow("AI Hand Tracking", frame)

        key = cv2.waitKey(1) & 0xFF

        # ---------------------------------
        # Save JSON (Press S)
        # ---------------------------------

        if key == ord("s"):

            extractor.print_landmarks(landmark_data)

            distance_calculator.print_distance(distance)

            json_saver.save(landmark_data)

        # ---------------------------------
        # Quit (Press Q)
        # ---------------------------------

        elif key == ord("q"):
            break

    # ----------------------------
    # Cleanup
    # ----------------------------

    detector.close()
    camera.release()
    cv2.destroyAllWindows()

    print("\nApplication Closed Successfully.")


if __name__ == "__main__":
    main()