from rasa.core.agent import Agent
from functools import lru_cache
import os
import glob


models_dir = "./rasa_data/models"


def get_latest_model():
    """"""
    all_models = glob.glob(models_dir + "*")
    latest_model_name = max(all_models, key=os.path.getctime)
    return latest_model_name


@lru_cache(maxsize=None)
def loda_rasa_model(use_latest_trained_model=True) -> Agent:
    """"""
    if use_latest_trained_model:
        model_path = get_latest_model()
    model = Agent.load(model_path=model_path)
    return model

async def parse_message(message:str):
    model = loda_rasa_model()
    result = await model.parse_message(message_data=message)
    return result