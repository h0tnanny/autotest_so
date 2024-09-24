import pytest
from http import HTTPStatus
from config import BASE_URL, HEADERS
from models.event.event_filter_model import EventFilter
from models.response_data import ResponseData
from models.user.user_data import UserData
from services.api_client import APIClient
from services.event_services import EvetServices

@pytest.fixture
def client() -> EvetServices:
    return EvetServices(APIClient(BASE_URL, HEADERS))

def get_user_by_id_test(service: EvetServices) -> None:
    user_id = '34bf203d-c03a-46f1-a59c-fb12b50f7f69'
    response: ResponseData = service.get_by_id(user_id)
    user: UserData = UserData.model_validate(response.data_json)

    assert response.data_response.status_code == HTTPStatus.OK
    assert user.id == user_id

def get_user_by_filter_empty_test(service: EvetServices) -> None:
    filter = EventFilter(0,0)
    response: ResponseData = service.get_by_filter(filter)
    user_list: list[UserData] = [UserData.model_validate(user) for user in response.data_response.json()]

    assert user_list.count() == 0
