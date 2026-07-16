"""
hyperparameter_study.py

Random Forest Hyperparameter Experiment

Studies the effect of:
- 50 trees
- 100 trees
- 200 trees

Generates:
hyperparameter_report.csv
"""


import time
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score
)


from .model_config import (
    TRAIN_DATASET,
    TEST_DATASET,
    RANDOM_STATE
)



class HyperparameterStudy:


    def __init__(self):

        self.results = []

        self.X_train = None
        self.y_train = None

        self.X_test = None
        self.y_test = None



    # --------------------------------------
    # Load Dataset
    # --------------------------------------

    def load_dataset(self):

        print("\nLoading Dataset...")

        train_df = pd.read_csv(
            TRAIN_DATASET
        )

        test_df = pd.read_csv(
            TEST_DATASET
        )


        self.X_train = train_df.drop(
            "label",
            axis=1
        )

        self.y_train = train_df["label"]


        self.X_test = test_df.drop(
            "label",
            axis=1
        )

        self.y_test = test_df["label"]


        print("Dataset Loaded")



    # --------------------------------------
    # Run Experiment
    # --------------------------------------

    def run(self):

        tree_values = [

            50,

            100,

            200

        ]


        for trees in tree_values:


            print("\n==============================")
            print(f"Training Random Forest ({trees} Trees)")
            print("==============================")


            model = RandomForestClassifier(

                n_estimators=trees,

                random_state=RANDOM_STATE,

                n_jobs=-1

            )


            start = time.time()


            model.fit(

                self.X_train,

                self.y_train

            )


            end = time.time()



            predictions = model.predict(

                self.X_test

            )


            accuracy = accuracy_score(

                self.y_test,

                predictions

            )


            f1 = f1_score(

                self.y_test,

                predictions,

                average="weighted"

            )


            result = {


                "Trees": trees,

                "Training Time": round(

                    end-start,

                    4

                ),


                "Accuracy": round(

                    accuracy,

                    4

                ),


                "F1 Score": round(

                    f1,

                    4

                )


            }


            self.results.append(result)



            print(result)



    # --------------------------------------
    # Save Report
    # --------------------------------------

    def save_report(self):


        df = pd.DataFrame(

            self.results

        )


        path = (

            "generated/"
            "hyperparameter_report.csv"

        )


        df.to_csv(

            path,

            index=False

        )


        print("\n==============================")
        print("REPORT GENERATED")
        print("==============================")

        print(df)

        print(f"\nSaved : {path}")




def main():


    study = HyperparameterStudy()


    study.load_dataset()

    study.run()

    study.save_report()



if __name__ == "__main__":

    main()