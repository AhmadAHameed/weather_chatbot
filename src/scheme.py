from pydantic import BaseModel


class Message(BaseModel):
    text: str

class City(BaseModel):
    text: str