"""
sentence_builder.py

Future Component

Builds words and sentences from
continuous gesture predictions.

Current Status:
Prototype for future live recognition.
"""


class SentenceBuilder:
    """
    Builds sentences from predicted gestures.
    """

    def __init__(self):

        self.words = []

        self.last_prediction = None

    # ---------------------------------------------------------
    # Add Prediction
    # ---------------------------------------------------------

    def add_prediction(self, prediction):
        """
        Store a predicted gesture.

        Consecutive duplicate predictions
        are ignored to reduce repetition.

        Args:
            prediction:
                Gesture or word predicted
                by the future sequence model.
        """

        if prediction != self.last_prediction:

            self.words.append(prediction)

            self.last_prediction = prediction

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

        self.last_prediction = None

    # ---------------------------------------------------------
    # Number of Words
    # ---------------------------------------------------------

    def word_count(self):
        """
        Return number of stored words.
        """

        return len(self.words)

    # ---------------------------------------------------------
    # Get Words
    # ---------------------------------------------------------

    def get_words(self):
        """
        Return all stored predictions.
        """

        return self.words