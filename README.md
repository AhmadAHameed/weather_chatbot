# Weather Chatbot using Botpress, Rasa & Python

This is a simple weather chatbot, created using Botpress for chatting, Rasa as a language model and Python as backend engine.
A short description of some technologies used in this simple project:

## 1- Rasa
- Used for NLU task to get user intent and extract entities from user messages.
- Most important rasa files needed for training rasa model are:
    - "config.yml"
    - "domain.yml"
    - "data/nlu.yml"
    you can read more about them and how they are used to train rasa model.
- Rasa can be used for chatting but we will use it as NLU engine and embed it in Botpress.

## 2- Botpress
- Used as chatbot platform
- the folder "botpress_data" contains some javascript files that can be used for botpress actions, these files can be a guidance and you should create your own files depending on the chatbot flow you want.

## 3- Python
- Used for backend tasks, for example to load the trained Rasa model, train the model, requesting external APIs to get some data, and many other tasks.
- FastAPI is used but you can use any other library such as Flask for routing.

## 4- Docker
- Containerizing the project files and data.
- Docker-compose for defining and running multi-container docker application.

### Note:
- Please notice that this is a very simple version for weather chatbot that cover few topics and intents, for this session we covered only "get_weather_realtime" in python and in botpress, we may cover other intents such as "get_weather_history" or "get_weather_forecast" in a later session, or you can create them, just create new routes for getting these info

- APIs used for this task are:
    - Weather API: To get weather info (realtime, forecast & history).
        "https://api.weatherapi.com/v1/current.json"
    
    - Map Quest API: To correct typos or suggest locations for chatbot user in case of typos in chatbot user locations.
        "http://www.mapquestapi.com/geocoding/v1/address"
