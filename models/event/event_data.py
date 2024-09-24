from pydantic import BaseModel
from models.user.user_data import UserData


class EventData(BaseModel):
    title: str
    date: str
    location: str
    partisipants: list[UserData] | None
