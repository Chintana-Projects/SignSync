# Future Live Recognition Pipeline

## Objective

The current SignSync AI engine recognizes static sign language gestures using a Random Forest classifier.

Future versions of the system will support continuous sign language recognition, where meaning depends on the movement of gestures across multiple frames.

---

# Proposed Architecture

```
Webcam Stream
      │
      ▼
Frame Capture
      │
      ▼
MediaPipe
      │
      ▼
Landmark Extraction
      │
      ▼
Temporal Buffer
      │
      ▼
Sequence Generator
      │
      ▼
Sequence Model
(LSTM / GRU / Transformer)
      │
      ▼
Gesture / Word Prediction
      │
      ▼
Sentence Formation
```

---

# Component Design

## 1. Webcam Stream

### Responsibility

Continuously captures frames from the webcam.

### Input

Live camera feed.

### Output

Video frames.

### Why Needed

Provides real-time input for gesture recognition.

---

## 2. Frame Capture

### Responsibility

Extracts individual frames from the webcam stream.

### Input

Video stream.

### Output

Single image frame.

### Why Needed

Allows every frame to be processed independently.

---

## 3. MediaPipe

### Responsibility

Detects hand landmarks.

### Input

Image frame.

### Output

21 hand landmarks.

### Why Needed

Extracts the hand pose for further processing.

---

## 4. Landmark Extraction

### Responsibility

Converts MediaPipe landmarks into structured landmark objects.

### Input

MediaPipe results.

### Output

21 landmark coordinates.

### Why Needed

Provides consistent landmark representation.

---

## 5. Temporal Buffer

### Responsibility

Stores the most recent landmark frames.

### Input

Current landmark frame.

### Output

Sequence of N landmark frames.

### Why Needed

Captures motion information across time.

---

## 6. Sequence Generator

### Responsibility

Converts buffered landmark frames into sequences suitable for deep learning models.

### Input

Temporal Buffer.

### Output

Sequence of landmark vectors.

### Why Needed

Prepares temporal data for sequence models.

---

## 7. Sequence Model

### Responsibility

Learns gesture motion across multiple frames.

Possible Models:

- LSTM
- GRU
- Transformer

### Input

Sequence of landmark vectors.

### Output

Gesture or word prediction.

### Why Needed

Recognizes dynamic gestures instead of single-frame gestures.

---

## 8. Gesture / Word Prediction

### Responsibility

Produces the recognized gesture or word.

### Input

Sequence Model output.

### Output

Predicted gesture.

### Why Needed

Converts learned temporal features into human-readable predictions.

---

## 9. Sentence Formation

### Responsibility

Combines consecutive predictions into meaningful sentences.

### Input

Gesture or word predictions.

### Output

Complete sentence.

Example:

HELLO

↓

HOW

↓

ARE

↓

YOU

↓

HELLO HOW ARE YOU

### Why Needed

Allows continuous sign language communication instead of isolated gesture recognition.

---

# Future Improvements

- Continuous live recognition
- Dynamic gesture recognition
- Word-level prediction
- Sentence-level prediction
- Context-aware correction
- Transformer-based sequence models
- Real-time streaming optimization