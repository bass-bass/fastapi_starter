import argparse
from util.logger import Logger
from util.config import Config
from model.ftmodel import FTModel

env = Config()
logger = Logger(__name__).get_logger()
# load model
ft_model = FTModel(env)

def evaluate_model(date: str):
    try:
        split = 2
        ft_model.evaluate_model(10, date, split)
    except Exception as e:
        logger.error("Failed to evaluate model.")
        logger.error(e)
    logger.info("successfully evaluate model!")

def make_data(date: str):
    try:
        ft_model.make_train_data(10, date)
    except Exception as e:
        logger.error("Failed to make train data.")
        logger.error(e)
    logger.info("successfully made train data!")

def make_model():
    try:
        ft_model.make_model()
    except Exception as e:
        logger.error("Failed to make model.")
        logger.error(e)
    logger.info("successfully made model!")

    try:
        ft_model.save_model()
    except Exception as e:
        logger.error("Failed to save model.")
        logger.error(e)
    logger.info("successfully saved model!")

def upload_model(date: str):
    try:
        ft_model.upload_model(date)
    except Exception as e:
        logger.error("Failed to upload model.")
        logger.error(e)
    logger.info("successfully uploaded model!")

def download_model(date: str):
    try:
        ft_model.download_model(date)
    except Exception as e:
        logger.error("Failed to download model.")
        logger.error(e)
    logger.info("successfully downloaded model!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name',
                        type=str,
                        help='set fuction name in this file')
    parser.add_argument('-d', '--date',
                        type=str,
                        help='target date')
    args = parser.parse_args()

    # 関数一覧を取得
    func_dict = {k: v for k, v in locals().items() if callable(v)}
    # 関数実行
    if (args.date==None):
        func_dict[args.function_name]()
    else:
        func_dict[args.function_name](args.date)