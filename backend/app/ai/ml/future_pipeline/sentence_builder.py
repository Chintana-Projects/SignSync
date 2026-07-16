"""
sentence_builder.py

Future Component

Builds words and sentences from
continuous gesture predictions.

Current Status:
Architecture Placeholder
"""


class SentenceBuilder:
    """
    Builds sentences from predicted gestures.
    """

    def __init__(self):

        self.words = []

    # ---------------------------------------------------------
    # Add Prediction
    # ---------------------------------------------------------

    def add_prediction(self, prediction):
        """
        Store a predicted gesture or word.

        Args:
            prediction:
                Gesture/word predicted by
                the future sequence model.
        """

        self.words.append(prediction)

    # ---------------------------------------------------------
    # Get Sentence
    # ---------------------------------------------------------

    def get_sentence(self):
        """
        Return the current sentence.
        """

        return " ".join(self.words)

    # ---------------------------------------------------------
    # Reset Sentence
    # ---------------------------------------------------------

    def clear(self):
        """
        Clear the current sentence.
        """

        self.words.clear()

    # ---------------------------------------------------------
    # Number of Words
    # ---------------------------------------------------------

    def word_count(self):
        """
        Return number of stored words.
        """

        return len(self.words)