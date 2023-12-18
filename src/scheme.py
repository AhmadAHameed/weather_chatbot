from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Location(BaseModel):
    location: str
    # text: str
