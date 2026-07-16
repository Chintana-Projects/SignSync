"""
train_model.py

Entry point for ML model training.

Responsibilities
----------------
1. Initialize the generic trainer.
2. Prepare the training pipeline.
3. Train the selected algorithm (when enabled).
"""

from .trainer import ModelTrainer


def main():

    trainer = ModelTrainer()

    # ----------------------------------
    # Prepare Training Pipeline
    # ----------------------------------

    trainer.prepare_pipeline()

    # ----------------------------------
    # Select Algorithm
    # ----------------------------------

    algorithm = "RandomForest"

    trainer.create_model(algorithm)

    # ----------------------------------
    # Uncomment when training is required
    # ----------------------------------

    # trainer.train()

    # results = trainer.evaluate()

    # trainer.save_model()

    # print(results)

    print("\n====================================")
    print("TRAINING PIPELINE READY")
    print("====================================")
    print(f"Selected Algorithm : {algorithm}")
    print("Training has NOT been executed.")


if __name__ == "__main__":
    main()