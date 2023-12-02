from fastapi import FastAPI
from src.scheme import Message, City
from src import api_requests
from src import resources

app = FastAPI()


@app.get("/")
async def root():
    """"""
    return {"result": "Root URL"}


@app.post("/nlu/parse")
async def parse_message(message: Message):
    """"""
    result = "Not Found"

    if message.text != "":
        result = await resources.parse_message(message.text)
        
    return {"result": result}


@app.post("/get_weather_now")
async def get_weather_now(city: City):
    """"""
    results = ""
    response = api_requests.get_weather_now(city)
    if response.status_code == 200:
        results = response.text
    return {"resulst": results}
