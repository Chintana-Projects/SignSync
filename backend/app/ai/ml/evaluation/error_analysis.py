"""
error_analysis.py

Generates confusion matrix
and finds most confused gestures.
"""

import json
import pandas as pd

from sklearn.metrics import confusion_matrix

import joblib

from ..training.model_config import (
    TEST_DATASET,
    MODEL_PATHS
)



class ErrorAnalyzer:


    def __init__(self):

        self.model = None

        self.test_df = None

        self.X_test = None

        self.y_test = None



    def load_data(self):

        print("\nLoading Test Dataset...")

        self.test_df = pd.read_csv(
            TEST_DATASET
        )


        self.X_test = self.test_df.drop(
            "label",
            axis=1
        )

        self.y_test = self.test_df["label"]


    def load_model(self):

        print("\nLoading Random Forest Model...")

        self.model = joblib.load(

            MODEL_PATHS["RandomForest"]

        )


    def analyze(self):

        print("\nGenerating Predictions...")

        predictions = self.model.predict(
            self.X_test
        )


        labels = sorted(
            self.y_test.unique()
        )


        cm = confusion_matrix(
            self.y_test,
            predictions,
            labels=labels
        )


        confusion = []


        for i in range(len(labels)):

            for j in range(len(labels)):

                if i != j and cm[i][j] > 0:

                    confusion.append({

                        "actual": labels[i],

                        "predicted": labels[j],

                        "count": int(cm[i][j])

                    })


        confusion = sorted(

            confusion,

            key=lambda x:x["count"],

            reverse=True

        )


        print("\nTop 5 Confused Gestures")

        for item in confusion[:5]:

            print(item)



        report = {

            "top_confusions": confusion[:5]

        }


        with open(

            "generated/error_analysis.json",

            "w"

        ) as file:

            json.dump(

                report,

                file,

                indent=4

            )


        return confusion[:5]



def main():

    analyzer = ErrorAnalyzer()

    analyzer.load_data()

    analyzer.load_model()

    analyzer.analyze()



if __name__ == "__main__":

    main()