from dataclasses import asdict
from models.response_data import ResponseData
from services.api_client import APIClient
from models import EventFilter, UserData


class EvetServices:
    def __init__(self, client: APIClient) -> None:
        self.__client = client

    def get_by_id(self, id: str) -> ResponseData:
        return self.__client.get(schema=UserData, endpoint=f'events/{id}')

    def get_by_filter(self, eventFilter: EventFilter) -> ResponseData:
        return self.__client.get(schema=list[UserData], endpoint='events/list', params=asdict(eventFilter))
