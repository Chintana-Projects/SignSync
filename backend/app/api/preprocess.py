"""
preprocess.py

Dataset Preprocessing API

Responsibilities
----------------
1. Expose dataset preprocessing endpoint.
2. Delegate preprocessing to PreprocessingService.
"""

from fastapi import APIRouter

from app.services.preprocessing_service import PreprocessingService

router = APIRouter()

# Change this path if your dataset is located elsewhere
DATASET_PATH = (
    r"C:\Users\DEll\.vscode\Sign\datasets"
    r"\ASL_Alphabet_Dataset\asl_alphabet_train"
)

preprocessing_service = PreprocessingService(DATASET_PATH)


@router.post("/preprocess")
def preprocess():
    """
    Trigger dataset preprocessing.
    """
    return preprocessing_service.preprocess()