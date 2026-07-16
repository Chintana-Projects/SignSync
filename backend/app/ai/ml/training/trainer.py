"""
trainer.py

Generic Model Trainer

Responsibilities
----------------
1. Load train/validation/test datasets.
2. Prepare features and labels.
3. Create the requested ML model.
4. Train the model.
5. Evaluate model performance.
6. Save trained model.

Supported Models
----------------
- Random Forest
- Decision Tree
- Support Vector Machine
"""

import time
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from .metrics import ModelMetrics

from .model_config import (
    TRAIN_DATASET,
    VALIDATION_DATASET,
    TEST_DATASET,
    MODEL_PATHS,
    RANDOM_FOREST_PARAMS,
    DECISION_TREE_PARAMS,
    SVM_PARAMS
)


class ModelTrainer:

    def __init__(self):

        self.algorithm = None

        self.train_df = None
        self.validation_df = None
        self.test_df = None

        self.X_train = None
        self.y_train = None

        self.X_validation = None
        self.y_validation = None

        self.X_test = None
        self.y_test = None

        self.model = None

        self.training_time = None

    # ==========================================================
    # STEP 1
    # Load Dataset
    # ==========================================================

    def load_datasets(self):

        print("\nLoading Datasets...")

        self.train_df = pd.read_csv(TRAIN_DATASET)

        self.validation_df = pd.read_csv(
            VALIDATION_DATASET
        )

        self.test_df = pd.read_csv(TEST_DATASET)

        print("Datasets Loaded Successfully")

        print(f"Training Samples   : {len(self.train_df)}")
        print(f"Validation Samples : {len(self.validation_df)}")
        print(f"Testing Samples    : {len(self.test_df)}")

    # ==========================================================
    # STEP 2
    # Prepare Dataset
    # ==========================================================

    def prepare_dataset(self):

        print("\nPreparing Dataset...")

        self.X_train = self.train_df.drop(
            "label",
            axis=1
        )

        self.y_train = self.train_df["label"]

        self.X_validation = self.validation_df.drop(
            "label",
            axis=1
        )

        self.y_validation = self.validation_df["label"]

        self.X_test = self.test_df.drop(
            "label",
            axis=1
        )

        self.y_test = self.test_df["label"]

        print("Dataset Prepared Successfully")

    # ==========================================================
    # STEP 3
    # Create Model
    # ==========================================================

    def create_model(self, algorithm):

        self.algorithm = algorithm

        print(f"\nCreating {algorithm} Model...")

        if algorithm == "RandomForest":

            self.model = RandomForestClassifier(
                **RANDOM_FOREST_PARAMS
            )

        elif algorithm == "DecisionTree":

            self.model = DecisionTreeClassifier(
                **DECISION_TREE_PARAMS
            )

        elif algorithm == "SVM":

            self.model = SVC(
                **SVM_PARAMS
            )

        else:

            raise ValueError(
                f"Unsupported Algorithm : {algorithm}"
            )

        print(f"{algorithm} Model Created")
    # ==========================================================
    # STEP 4
    # Train Model
    # ==========================================================

    def train(self):

        print(f"\nTraining {self.algorithm}...")

        start_time = time.time()

        self.model.fit(
            self.X_train,
            self.y_train
        )

        end_time = time.time()

        self.training_time = round(
            end_time - start_time,
            4
        )

        print(f"Training Completed ({self.training_time} sec)")

    # ==========================================================
    # STEP 5
    # Evaluate Model
    # ==========================================================

    def evaluate(self):

        print(f"\nEvaluating {self.algorithm}...")

        predictions = self.model.predict(
            self.X_test
        )

        metrics = ModelMetrics.evaluate(
            self.y_test,
            predictions
        )

        print("\n====================================")
        print(f"{self.algorithm} Evaluation")
        print("====================================")

        print(f"Accuracy  : {metrics['accuracy']}")
        print(f"Precision : {metrics['precision']}")
        print(f"Recall    : {metrics['recall']}")
        print(f"F1 Score  : {metrics['f1_score']}")

        return {

            "algorithm": self.algorithm,

            "training_time": self.training_time,

            "accuracy": metrics["accuracy"],

            "precision": metrics["precision"],

            "recall": metrics["recall"],

            "f1_score": metrics["f1_score"]

        }

    # ==========================================================
    # STEP 6
    # Save Model
    # ==========================================================

    def save_model(self):

        print(f"\nSaving {self.algorithm} Model...")

        model_path = MODEL_PATHS[self.algorithm]

        joblib.dump(
            self.model,
            model_path
        )

        print("Model Saved Successfully")

        print(f"Location : {model_path}")

    # ==========================================================
    # STEP 7
    # Prepare Pipeline
    # ==========================================================

    def prepare_pipeline(self):

        self.load_datasets()

        self.prepare_dataset()

        print("\n====================================")
        print("TRAINING PIPELINE READY")
        print("====================================")

    # ==========================================================
    # STEP 8
    # Complete Training Pipeline
    # ==========================================================

    def run(self, algorithm):
        """
        Train and evaluate the selected algorithm.

        Assumes prepare_pipeline() has already been called.
        """

        self.create_model(algorithm)

        self.train()

        results = self.evaluate()

        self.save_model()

        return results