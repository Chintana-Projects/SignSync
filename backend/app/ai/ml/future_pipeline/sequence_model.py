"""
sequence_model.py

Future Component

Placeholder for future sequence-based
gesture recognition models.

Possible Models
---------------
- LSTM
- GRU
- Transformer

Current Status:
Architecture Placeholder
"""


class SequenceModel:
    """
    Future temporal deep learning model.
    """

    def __init__(self):

        self.model_name = "Future LSTM/GRU/Transformer"

    # ---------------------------------------------------------
    # Load Model
    # ---------------------------------------------------------

    def load(self):
        """
        Placeholder for loading
        the future sequence model.
        """

        print(f"{self.model_name} not implemented.")

    # ---------------------------------------------------------
    # Predict Sequence
    # ---------------------------------------------------------

    def predict(self, sequence):
        """
        Predict gesture/word from a
        sequence of landmark frames.

        Args:
            sequence:
                Sequence generated from
                TemporalBuffer.

        Returns:
            Placeholder prediction.
        """

        return "Future Prediction"

    # ---------------------------------------------------------
    # Model Information
    # ---------------------------------------------------------

    def info(self):
        """
        Returns model information.
        """

        return {

            "model": self.model_name,

            "status": "Architecture Only",

            "implemented": False

        }