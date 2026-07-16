"""
temporal_buffer.py

Future Component

Stores the latest N landmark frames
for sequence-based gesture recognition.

Current Status:
Architecture Placeholder
"""


class TemporalBuffer:
    """
    Stores a rolling window of landmark frames.
    """

    def __init__(self, max_frames=30):

        self.max_frames = max_frames

        self.frames = []

    def add_frame(self, landmarks):

        self.frames.append(landmarks)

        if len(self.frames) > self.max_frames:

            self.frames.pop(0)

    def get_sequence(self):

        return self.frames

    def clear(self):

        self.frames.clear()

    def is_ready(self):

        return len(self.frames) == self.max_frames