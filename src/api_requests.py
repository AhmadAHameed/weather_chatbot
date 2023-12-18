import requests
import os
from src.logger import logger
from src.scheme import Location


WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
MAP_QUEST_URL = "http://www.mapquestapi.com/geocoding/v1/address"

# WEATHER_API_KEY = "e8b64c1cd9724aee8b2101826232111"
# MAP_QUEST_API_KEY = "cCwXbsprpjWxWQxej5pKyVXiDTfC43fk"


def read_env_key(key_name: str, default=""):
    key = os.getenv(key_name, default)
    return key if key else logger.info(f'env key: "{key_name}" is not found')


def get_weather_realtime(location: str, lang="en"):
    weather_api_key = read_env_key("WEATHER_API_KEY", "")
    params = {"q": location, "lang": lang, "key": weather_api_key}
    header = {}
    payload = ""

    response = requests.request(
        "POST", url=WEATHER_URL, headers=header, data=payload, params=params
    )

    if response.status_code == 200:
        if (
            str(response.json()["location"]["name"]).lower()
            == location.lower()
        ):
            return {"message": "ok", "content": response.json()}
        else:
            nearest_location = get_nearest_location_name(location)
            return {
                "message": "different_location",
                "content": {
                    "input_location": location,
                    "found_location": response.json()["location"]["name"],
                    "nearest_location": nearest_location,
                },
            }

    if not location_is_valid(response):
        nearest_location = get_nearest_location_name(location)
        return {
            "message": "location_error",
            "content": {
                "input_location": location,
                "nearest_location": nearest_location,
            },
        }

    else:
        return {"message": "other_error", "content": response.json()}

    # elif not check_valid_location():
    #     nearest_location = get_nearest_location_name()

    return response


def location_is_valid(response: requests.Response):
    if (
        response.json()["error"]["code"] == 1006
        or "no matching location found"
        in str(response.json()["error"]["message"]).lower()
    ):
        return False
    else:
        return True


def get_nearest_location_name(location):
    """"""
    map_quest_api_key = read_env_key(
        "MAP_QUEST_API_KEY", ""
    )
    params = {"location": location, "key": map_quest_api_key}
    headers = {}
    payload = ""

    response = requests.request(
        "POST", url=MAP_QUEST_URL, headers=headers, data=payload, params=params
    )

    if response.status_code == 200:
        nearest_location = response.json()["results"][0]["locations"][0]["adminArea5"]
        return nearest_location
    else:
        return
