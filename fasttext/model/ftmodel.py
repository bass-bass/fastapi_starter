import time
import numpy as np
import pandas as pd
from io import BytesIO

import fasttext as ft
from util.logger import Logger
from util.storage import GCSWrapper

class FTModel:
    def __init__(self, config):
        self.config = config
        self.logger = Logger(__name__).get_logger()
        self.storage = GCSWrapper(config.credential_path, config.bucket_name)
        self.lr = 0.5
        self.dim = 200
        self.epoch = 25
        self.wordNgrams = 2
    
    def evaluate_model(self, divideNum:int, date:str, split:int):
        """
        
        BATCH
        0. modelの評価
        """
        train = self.get_data_by_range(date, 0, divideNum-split)
        valid = self.get_data_by_range(date, divideNum-split, divideNum)
        df = pd.read_table(BytesIO(train))
        df.to_csv(self.config.local_data_train_path, sep="\n", index=False, header=False)
        df = pd.read_table(BytesIO(valid))
        df.to_csv(self.config.local_data_valid_path, sep="\n", index=False, header=False)

        # train
        start = time.perf_counter()
        self.model = ft.train_supervised(
            input=self.config.local_data_train_path,
            lr=self.lr,
            dim=self.dim,
            epoch=self.epoch,
            wordNgrams=self.wordNgrams)
        end = time.perf_counter()
        process_sec = end - start
        process_min = int(process_sec/60)
        self.logger.info("training finished. " + str(process_min) + " min")

        # evaluate
        start = time.perf_counter()
        result = self.model.test(self.config.local_data_valid_path)
        end = time.perf_counter()
        process_sec = end - start
        process_min = int(process_sec/60)
        self.logger.info("evaluate finished. " + str(process_min) + " min")
        self.logger.info("valid data count -> " + str(result[0]))
        self.logger.info("precision -> " + str(result[1]))
        self.logger.info("recall -> " + str(result[2]))
        print("precision -> " + str(result[1]))
        print("recall -> " + str(result[2]))

    def make_train_data(self, divideNum: int, date: str):
        """
        BATCH
        1. trainデータのダウンロード
        """
        content = self.get_data_by_range(date, 0, divideNum)
        
        df = pd.read_table(BytesIO(content))
        df.to_csv(self.config.local_data_path, sep="\n", index=False, header=False)
        self.logger.info("train data downloaded.")
        self.logger.info("date -> " + date + " path -> " + self.config.local_data_path)


    def make_model(self):
        """
        BATCH
        2. modelの学習
        """
        start = time.perf_counter()
        self.model = ft.train_supervised(
            input=self.config.local_data_path,
            lr=self.lr,
            dim=self.dim,
            epoch=self.epoch,
            wordNgrams=self.wordNgrams)
        end = time.perf_counter()
        process_sec = end - start
        process_min = int(process_sec/60)
        self.logger.info("training finished. " + str(process_min) + " min")

        self.save_model()
        self.logger.info("model saved to local.")

    def save_model(self):
        """
        BATCH
        3. 作成したmodelをlocalへ保存
        """
        self.model.save_model(self.config.local_model_path)

    def upload_model(self, date: str):
        """
        BATCH
        4. localのmodelをGCSへアップロード
        """
        gcs_model_path = self.get_gcs_model_path(date)
        self.storage.upload_file(self.config.local_model_path, gcs_model_path)
        self.logger.info("model uploaded. path -> " + gcs_model_path)

    def download_model(self, date: str):
        """
        BATCH
        5. GCSのmodelをlocalへダウンロード
        """
        local_model_path = self.config.local_model_path
        gcs_model_path = self.get_gcs_model_path(date)
        self.storage.download_file(local_model_path, gcs_model_path)

    def load_model(self):
        """
        API
        6. localのモデルをロード
        """
        self.model = ft.load_model(self.config.local_model_path)

    def predict(self, text: str):
        """
        API
        7. ロードしたmodelでの推論
        """
        result = self.model.predict(text,5)
        class_id = int(result[0][0].replace("__label__",""))
        prob = result[1][0]
        #variance = np.var(result[1])
        return {"class": class_id, "prob":prob}

    def get_data_by_range(self, date:str, start:int, end:int):
        content = bytes()
        for i in range(start, end):
            gcs_data_path = self.get_gcs_data_path(date, i)
            content += self.storage.get_content_as_string(gcs_data_path)
        return content

    def get_gcs_model_path(self, date: str):
        gcs_model_path = self.config.gcs_model_path.replace("{date}",date)
        return gcs_model_path

    def get_gcs_data_path(self, date: str, num: int):
        gcs_data_path = self.config.gcs_data_path.replace("{date}",date).replace("{number}",str(num))
        return gcs_data_path
