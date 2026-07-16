"""
inference_benchmark.py

Measures Random Forest inference performance.
"""

import time
import os
import joblib
import pandas as pd
import tracemalloc


from ..training.model_config import (
    TEST_DATASET,
    MODEL_PATHS
)



class InferenceBenchmark:


    def __init__(self):

        self.model = None
        self.X_test = None


    # ---------------------------------
    # Load model and data
    # ---------------------------------

    def load(self):

        print("\nLoading Model...")

        self.model = joblib.load(
            MODEL_PATHS["RandomForest"]
        )


        print("Loading Test Data...")

        test_df = pd.read_csv(
            TEST_DATASET
        )


        self.X_test = test_df.drop(
            "label",
            axis=1
        )



    # ---------------------------------
    # Benchmark
    # ---------------------------------

    def run(self):

        print("\nRunning Inference Benchmark...")


        samples = len(self.X_test)


        # warm-up prediction

        self.model.predict(
            self.X_test.iloc[:10]
        )


        tracemalloc.start()


        start = time.time()


        predictions = self.model.predict(
            self.X_test
        )


        end = time.time()


        current, peak = tracemalloc.get_traced_memory()


        tracemalloc.stop()



        total_time = end - start


        avg_time_ms = (
            total_time / samples
        ) * 1000



        throughput = (
            samples / total_time
        )


        model_size = os.path.getsize(

            MODEL_PATHS["RandomForest"]

        ) / (1024 * 1024)



        report = {

            "total_predictions": samples,

            "average_inference_time_ms":
                round(avg_time_ms, 4),

            "throughput_predictions_per_second":
                round(throughput, 2),

            "peak_memory_mb":
                round(
                    peak / (1024*1024),
                    2
                ),

            "model_size_mb":
                round(model_size, 2)

        }



        print("\n==============================")
        print("INFERENCE BENCHMARK")
        print("==============================")

        for key,value in report.items():

            print(
                f"{key}: {value}"
            )


        return report



def main():

    benchmark = InferenceBenchmark()

    benchmark.load()

    benchmark.run()



if __name__ == "__main__":

    main()