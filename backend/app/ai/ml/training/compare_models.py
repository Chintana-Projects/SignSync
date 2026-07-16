"""
compare_models.py

Compares multiple machine learning algorithms.

Algorithms
----------
1. Random Forest
2. Decision Tree
3. Support Vector Machine

Outputs
-------
comparison_report.csv
"""

import pandas as pd

from .trainer import ModelTrainer


class ModelComparator:

    def __init__(self):

        self.algorithms = [

            "RandomForest",

            "DecisionTree",

            "SVM"

        ]

        self.results = []

    # -----------------------------------------------------
    # Compare Models
    # -----------------------------------------------------

    def compare(self):

        print("\n==============================")
        print("MODEL COMPARISON")
        print("==============================")

        trainer = ModelTrainer()

        # Load dataset ONLY ONCE
        trainer.prepare_pipeline()

        for algorithm in self.algorithms:

            print(f"\nTraining {algorithm}...")

            result = trainer.run(algorithm)

            self.results.append(result)

        self.save_report()

    # -----------------------------------------------------
    # Save Report
    # -----------------------------------------------------

    def save_report(self):

        df = pd.DataFrame(self.results)

        df.rename(

            columns={

                "algorithm": "Algorithm",

                "training_time": "Training Time",

                "accuracy": "Accuracy",

                "precision": "Precision",

                "recall": "Recall",

                "f1_score": "F1 Score"

            },

            inplace=True

        )

        output_path = "generated/comparison_report.csv"

        df.to_csv(

            output_path,

            index=False

        )

        print("\n==============================")
        print("COMPARISON REPORT GENERATED")
        print("==============================")

        print(df)

        print(f"\nSaved to: {output_path}")


def main():

    comparator = ModelComparator()

    comparator.compare()


if __name__ == "__main__":
    main()