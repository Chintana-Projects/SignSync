# Error Analysis Report

## Model

Random Forest Classifier

## Dataset

ASL Alphabet Dataset

Features:
- MediaPipe Hand Landmarks
- 21 landmarks
- 63 features (x, y, z coordinates)

---

# Top Confused Gestures

| Actual | Predicted | Count |
|--------|-----------|-------|
| N | M | 14 |
| M | N | 7 |
| O | C | 7 |
| V | U | 7 |
| S | E | 4 |

---

# Analysis of Errors

## 1. N and M Confusion

The gestures N and M have very similar hand configurations.

Possible reasons:

- Both gestures involve folded fingers.
- Small changes in finger position can change the gesture.
- The model may find difficulty distinguishing finger placement.


## 2. O and C Confusion

The gestures O and C have similar curved hand shapes.

Possible reasons:

- Both contain a rounded finger arrangement.
- Hand orientation changes can make them appear similar.
- Different camera angles may affect landmark positions.


## 3. V and U Confusion

The gestures V and U are visually similar.

Possible reasons:

- Both use two extended fingers.
- The difference depends mainly on finger separation.
- Small landmark variations can cause incorrect classification.


## 4. S and E Confusion

These gestures have similar closed-fist structures.

Possible reasons:

- Fingers are partially folded in both gestures.
- Thumb position affects classification.
- Occlusion between fingers can reduce landmark accuracy.


# Overall Observation

The Random Forest model performs well with high accuracy.

Most errors occur between gestures having similar finger positions.

The major causes of confusion are:

- Similar hand shapes
- Small finger position differences
- Hand orientation variation
- Partial finger occlusion
- Dataset variations