"""
metrics.py

Model Evaluation Metrics

Responsibilities
----------------
1. Calculate Accuracy
2. Calculate Precision
3. Calculate Recall
4. Calculate F1 Score
5. Return all evaluation metrics
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


class ModelMetrics:
    """
    Calculates evaluation metrics for classification models.
    """

    @staticmethod
    def evaluate(y_true, y_pred):
        """
        Evaluate model predictions.

        Args:
            y_true : Actual labels
            y_pred : Predicted labels

        Returns:
            dict
        """

        metrics = {

            "accuracy": round(
                accuracy_score(y_true, y_pred),
                4
            ),

            "precision": round(
                precision_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0
                ),
                4
            ),

            "recall": round(
                recall_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0
                ),
                4
            ),

            "f1_score": round(
                f1_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0
                ),
                4
            )

        }

        return metrics


def main():
    """
    Example usage.
    """

    y_true = ["A", "B", "C", "A", "B"]
    y_pred = ["A", "B", "A", "A", "C"]

    results = ModelMetrics.evaluate(
        y_true,
        y_pred
    )

    print("\n==============================")
    print("MODEL METRICS")
    print("==============================")

    for metric, value in results.items():
        print(f"{metric:12}: {value}")


if __name__ == "__main__":
    main()