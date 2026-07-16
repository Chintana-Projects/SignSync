"""
sequence_generator.py

Future Component

Converts buffered landmark frames into
a sequence suitable for temporal models.

Current Status:
Prototype for future LSTM / GRU integration.
"""

import numpy as np


class SequenceGenerator:
    """
    Generates sequence tensors from buffered frames.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Generate Sequence
    # ---------------------------------------------------------

    def generate(self, frames):
        """
        Convert buffered landmark frames into
        a sequence tensor.

        Args:
            frames:
                List of 63-dimensional landmark vectors.

        Returns:
            NumPy array of shape:
            (number_of_frames, 63)
        """

        return np.array(
            frames,
            dtype=np.float32
        )

    # ---------------------------------------------------------
    # Sequence Length
    # ---------------------------------------------------------

    def sequence_length(self, sequence):
        """
        Returns the number of frames
        in the generated sequence.
        """

        return len(sequence)

    # ---------------------------------------------------------
    # Sequence Shape
    # ---------------------------------------------------------

    def sequence_shape(self, sequence):
        """
        Returns the shape of the sequence tensor.

        Example:
            (20, 63)
        """

        return sequence.shape

    # ---------------------------------------------------------
    # Check if Sequence is Ready
    # ---------------------------------------------------------

    def is_ready(self, sequence, required_length=20):
        """
        Checks whether enough frames
        have been collected.

        Returns:
            True if sequence contains
            at least required_length frames.
        """

        return len(sequence) >= required_length