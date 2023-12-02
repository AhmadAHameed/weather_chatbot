# Pull official base image
FROM python:3.10.13-slim

RUN mkdir -p /usr/weather_chatbot/app
WORKDIR /usr/weather_chatbot/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y curl software-properties-common libpq-dev build-essential libssl-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "uvicorn", "main:app","--host","0.0.0.0", "--port", "8000", "--workers", "1"  ]