from pydantic import BaseModel
from models.page_info_data import PageInfo


class EventFilter(BaseModel, PageInfo):
    date: str | None
    title: str | None
