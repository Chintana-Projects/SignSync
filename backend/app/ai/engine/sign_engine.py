"""
sign_engine.py

Main production interface for SignSync AI Engine.

Workflow:

Image
 ↓
Hand Detection
 ↓
Landmark Extraction
 ↓
Feature Validation
 ↓
Normalization
 ↓
Feature Conversion
 ↓
Model Prediction
 ↓
Confidence Calculation
 ↓
Confidence Threshold
 ↓
Logging
 ↓
PredictionResult
"""


import time


from app.ai.ml.inference.hand_detector import (
    HandDetector
)


from app.ai.ml.preprocessing.feature_validator import (
    FeatureValidator
)


from app.ai.ml.preprocessing.data_normalizer import (
    DataNormalizer
)


from app.ai.ml.inference.feature_converter import (
    FeatureConverter
)


from app.ai.ml.inference.predictor import (
    Predictor
)


from app.ai.ml.inference.confidence import (
    ConfidenceCalculator
)


from app.ai.ml.models.model_loader import (
    ModelLoader
)


from app.ai.engine.logger import (
    InferenceLogger
)


from app.ai.engine.prediction_result import (
    PredictionResult
)



class SignLanguageEngine:
    """
    Production AI Engine.

    Public interface:

        predict(image)

    Returns:

        PredictionResult
    """



    def __init__(self):

        print(
            "Initializing SignSync AI Engine..."
        )


        # ---------------------------------
        # Hand Processing Components
        # ---------------------------------

        self.hand_detector = HandDetector()


        self.validator = FeatureValidator()


        self.normalizer = DataNormalizer()


        self.converter = FeatureConverter()



        # ---------------------------------
        # Model Components
        # ---------------------------------

        self.model = ModelLoader().load(
            "RandomForest"
        )


        self.predictor = Predictor(
            self.model
        )


        self.confidence_calculator = (
            ConfidenceCalculator()
        )



        # ---------------------------------
        # Metadata
        # ---------------------------------

        self.model_version = "RF_v1"


        self.logger = InferenceLogger()


        print(
            "AI Engine Ready"
        )



    # ==================================================
    # MAIN PREDICTION INTERFACE
    # ==================================================

    def predict(self, image):
        """
        Predict sign gesture from image.

        Input:
            OpenCV image

        Output:
            PredictionResult
        """


        start_time = time.time()



        # ---------------------------------
        # STEP 1
        # Detect Hand Landmarks
        # ---------------------------------

        landmarks = self.hand_detector.detect(
            image
        )



        # No hand detected

        if landmarks is None:


            return PredictionResult(

                gesture="Nothing",

                confidence=0,

                model_version=self.model_version,

                inference_time_ms=0,

                status="no_hand"

            )



        # ---------------------------------
        # STEP 2
        # Validate Landmarks
        # ---------------------------------

        valid = self.validator.validate(
            landmarks
        )



        if not valid:


            return PredictionResult(

                gesture="Nothing",

                confidence=0,

                model_version=self.model_version,

                inference_time_ms=0,

                status="invalid_landmarks"

            )



        # ---------------------------------
        # STEP 3
        # Normalize Landmarks
        # ---------------------------------

        normalized_landmarks = (
            self.normalizer.normalize(
                landmarks
            )
        )



        # ---------------------------------
        # STEP 4
        # Convert to 63 Features
        # ---------------------------------

        features = self.converter.convert(
            normalized_landmarks
        )
                # ---------------------------------
        # STEP 5
        # Model Prediction
        # ---------------------------------

        prediction = self.predictor.predict(
            features
        )



        # ---------------------------------
        # STEP 6
        # Confidence Calculation
        # ---------------------------------

        confidence = (
            self.confidence_calculator.calculate(
                self.model,
                features
            )
        )



        # ---------------------------------
        # STEP 7
        # Apply Confidence Threshold
        # ---------------------------------

        prediction = (
            self.confidence_calculator.apply_threshold(
                prediction,
                confidence
            )
        )



        # ---------------------------------
        # STEP 8
        # Calculate Inference Time
        # ---------------------------------

        end_time = time.time()


        inference_time = (
            end_time - start_time
        ) * 1000



        # ---------------------------------
        # STEP 9
        # Log Inference Metadata
        # ---------------------------------

        self.logger.log(

            prediction=prediction,

            confidence=confidence,

            model_version=self.model_version,

            inference_time_ms=inference_time,

            status="success"

        )



        # ---------------------------------
        # STEP 10
        # Return Prediction Result
        # ---------------------------------

        return PredictionResult(

            gesture=prediction,

            confidence=round(
                float(confidence),
                4
            ),

            model_version=self.model_version,

            inference_time_ms=round(
                float(inference_time),
                4
            ),

            status="success"

        )