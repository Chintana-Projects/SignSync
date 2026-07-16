"""
model_config.py

Configuration for ML model training.

Responsibilities
----------------
1. Store dataset paths.
2. Store model save locations.
3. Store training parameters.
4. Store algorithm hyperparameters.
"""

from pathlib import Path

# ==========================================================
# Base Directory
# ==========================================================
BASE_DIR = Path(__file__).resolve().parents[5]
# ==========================================================
# Dataset Paths
# ==========================================================

GENERATED_DIR = BASE_DIR / "generated"

TRAIN_DATASET = GENERATED_DIR / "train.csv"
VALIDATION_DATASET = GENERATED_DIR / "validation.csv"
TEST_DATASET = GENERATED_DIR / "test.csv"

# ==========================================================
# Model Save Directory
# ==========================================================

MODEL_DIR = (
    BASE_DIR
    / "backend"
    / "app"
    / "ai"
    / "ml"
    / "models"
)

MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# Model filenames

MODEL_PATHS = {

    "RandomForest":
        MODEL_DIR / "random_forest.pkl",

    "DecisionTree":
        MODEL_DIR / "decision_tree.pkl",

    "SVM":
        MODEL_DIR / "svm.pkl"

}

# ==========================================================
# Common Training Parameters
# ==========================================================

RANDOM_STATE = 42

# ==========================================================
# Random Forest Hyperparameters
# ==========================================================

RANDOM_FOREST_PARAMS = {

    "n_estimators": 100,

    "max_depth": None,

    "min_samples_split": 2,

    "min_samples_leaf": 1,

    "random_state": RANDOM_STATE,

    "n_jobs": -1

}

# ==========================================================
# Decision Tree Hyperparameters
# ==========================================================

DECISION_TREE_PARAMS = {

    "criterion": "gini",

    "max_depth": None,

    "min_samples_split": 2,

    "min_samples_leaf": 1,

    "random_state": RANDOM_STATE

}

# ==========================================================
# Support Vector Machine Hyperparameters
# ==========================================================

SVM_PARAMS = {

    "kernel": "rbf",

    "C": 1.0,

    "gamma": "scale"

}