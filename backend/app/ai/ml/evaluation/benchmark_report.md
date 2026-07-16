# Inference Benchmark Report


## Model

Random Forest Classifier


## Dataset

Test Dataset:

ASL Alphabet Landmark Dataset

Samples Tested:

15208


## Performance Metrics


| Metric | Value |
|---|---|
| Average inference time | 0.0148 ms |
| Throughput | 67781.04 predictions/sec |
| Peak memory usage | 34.79 MB |
| Model size | 227.49 MB |


# Real-Time Suitability Analysis


The Random Forest model is suitable for real-time webcam-based sign recognition.

Reasons:

## 1. Low Prediction Latency

The average inference time is 0.0148 milliseconds per prediction.

This indicates that the model can classify gestures extremely quickly.


## 2. High Throughput

The model achieved approximately 67,781 predictions per second.

This is significantly higher than the requirement for webcam-based recognition, which normally operates around 30-60 FPS.


## 3. Memory Requirement

Peak memory consumption during inference was 34.79 MB.

This is acceptable for desktop-based real-time applications.


## 4. Model Size

The model size is 227.49 MB.

Although the file size is large, it is acceptable for a desktop learning platform.

For deployment on low-resource devices, model compression or optimization can be considered.


# Conclusion

The Random Forest model provides a good balance between accuracy and inference speed.

Based on the benchmark results, the model is suitable for integration into the SignSync real-time webcam recognition system.