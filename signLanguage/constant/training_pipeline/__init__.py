import os 

ARTIFACTS_DIR : str = "artifacts"

# data ingestion related constants

DATA_INGESTION_DIR_NAME : str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_NAME : str = "feature_store"

DATA_DOWNLOAD_URL : str = "https://github.com/mirzaumar28/random/raw/refs/heads/main/sign_lang.zip"

#  data validation related constants

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "valid", "data.yaml"]

#  model trainer related constants

MODEL_TRAINER_DIR_NAME : str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS : int = 300

MODEL_TRAINER_BATCH_SIZE : int = 16


#  model pusher related constants

BUCKET_NAME = "sign-lang-2025-umar"
S3_MODEL_NAME = "best.pt"
