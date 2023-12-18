from fastapi import FastAPI
from src.scheme import Message, Location
from src import api_requests
from src import resources
from uvicorn import run

app = FastAPI()


@app.get("/")
async def root():
    """"""
    return {"result": "Root URL"}


@app.post("/nlu/parse")
async def parse_message(message: Message):
    """"""
    result = "Not Found"

    if message.message != "":
        result = await resources.parse_message(message.message)

    return {"result": result}


@app.post("/get_weather_realtime")
async def get_weather_realtime(location: Location, language="en"):
    """"""
    result = api_requests.get_weather_realtime(location.location, language)

    return result


if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True)
