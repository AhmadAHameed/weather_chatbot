import requests
import os
from src.logger import logger


weather_api_key = os.getenv("weather_api_key", "")
if weather_api_key == "":
    logger.info("weather_api_key not found")


def get_weather_now(city: str, lang="en", key=weather_api_key):
    base_url = "https://api.weatherapi.com/"
    url_version = "v1/current.json"
    url = base_url + url_version
    params = {"q": city, "lang": lang, "key": key}
    header = {}
    payload = ""

    response = requests.request(
        "POST", url=url, headers=header, data=payload, params=params
    )
    return response
