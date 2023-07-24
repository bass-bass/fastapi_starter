from fastapi import FastAPI
from fastapi import HTTPException

from util.logger import Logger
from util.config import Config
from model.ftmodel import FTModel

app = FastAPI()

env = Config()
logger = Logger(__name__).get_logger()

# load model
try:
    ft_model = FTModel(env)
    ft_model.load_model()
except Exception as e:
    logger.error("Failed to load model")
    logger.error(e)
    raise HTTPException(status_code=500, detail=e)


@app.get("/")
def root():
    text = "これ は テスト です"
    class_id = ft_model.predict(text)
    return {"class": class_id}

@app.get("/classify")
def predict(text: str):
    try:
        result = ft_model.predict(text)
    except Exception as e:
        logger.error("Failed to predict text -> " + text)
        logger.error(e)
        raise HTTPException(status_code=500, detail=e)
    #logger.info(str(result["class"]) + " -> " + text)
    return result
