import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv("resources/.env")
        self.credential_path = os.environ['CREDENTIAL_PATH']
        self.bucket_name = os.environ['BUCKET_NAME']
        self.gcs_model_path = os.environ['GCS_MODEL_PATH']
        self.local_model_path = os.environ['LOCAL_MODEL_PATH']
        self.gcs_data_path = os.environ['GCS_DATA_PATH']
        self.local_data_path = os.environ['LOCAL_DATA_PATH']
        self.local_data_train_path = os.environ['LOCAL_DATA_TRAIN_PATH']
        self.local_data_valid_path = os.environ['LOCAL_DATA_VALID_PATH']