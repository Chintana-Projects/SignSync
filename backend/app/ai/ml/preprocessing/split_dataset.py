"""
split_dataset.py

Responsibilities
----------------
1. Read normalized_landmarks.csv.
2. Perform a stratified train/validation/test split.
3. Save train.csv, validation.csv and test.csv.
4. Display class distribution information.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split


class DatasetSplitter:

    def __init__(
        self,
        input_csv="generated/normalized_landmarks.csv",
        output_dir="generated"
    ):

        self.input_csv = input_csv
        self.output_dir = output_dir

    def split(self):

        print("\n==============================")
        print("SPLITTING DATASET")
        print("==============================\n")

        df = pd.read_csv(self.input_csv)

        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        # -----------------------------
        # 80% Train
        # 20% Temp
        # -----------------------------

        X_train, X_temp, y_train, y_temp = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        # -----------------------------
        # Split Temp into
        # 10% Validation
        # 10% Test
        # -----------------------------

        X_validation, X_test, y_validation, y_test = train_test_split(
            X_temp,
            y_temp,
            test_size=0.50,
            random_state=42,
            stratify=y_temp
        )

        train_df = pd.concat([X_train, y_train], axis=1)
        validation_df = pd.concat([X_validation, y_validation], axis=1)
        test_df = pd.concat([X_test, y_test], axis=1)

        os.makedirs(self.output_dir, exist_ok=True)

        train_df.to_csv(
            os.path.join(self.output_dir, "train.csv"),
            index=False
        )

        validation_df.to_csv(
            os.path.join(self.output_dir, "validation.csv"),
            index=False
        )

        test_df.to_csv(
            os.path.join(self.output_dir, "test.csv"),
            index=False
        )

        print("Dataset split completed successfully.\n")

        print(f"Training Samples   : {len(train_df)}")
        print(f"Validation Samples : {len(validation_df)}")
        print(f"Testing Samples    : {len(test_df)}")

        print("\nGesture Class Distribution\n")
        print(df["label"].value_counts().sort_index())

        return train_df, validation_df, test_df


def main():

    splitter = DatasetSplitter()

    splitter.split()


if __name__ == "__main__":
    main()