from typing import Type
from pydantic import BaseModel
import requests
import requests.api
import requests.structures
from enums.http_method import HttpMethod
from models.response_data import ResponseData


class APIClient:
    def __init__(self, url: str, headers = None) -> None:
        self.url = url
        self.headers = headers or {}
        requests.session()

    def execute(self, method: HttpMethod, schema: Type[BaseModel] | None, endpoint: str, params : dict | None, data: Type[BaseModel] | None) -> ResponseData:
        url: str = f"{self.url}/{endpoint}"
        response = requests.request(method=method, url=url, params=params, headers=self.headers, data=data)
        self.__validation_response(schema, response) if schema is not None else None

        return ResponseData(data_response=response, data_json=response.json())

    def get(self, schema: Type[BaseModel] | None, endpoint: str, params : dict | None, data: Type[BaseModel] | None) -> requests.Response:
        return self.execute(HttpMethod.GET, schema, endpoint, params, data)

    def post(self, schema: Type[BaseModel] | None, endpoint: str, params : dict | None, data: Type[BaseModel] | None) -> requests.Response:
        return self.execute(HttpMethod.POST, schema, endpoint, params, data)

    def put(self, schema: Type[BaseModel] | None, endpoint: str, params : dict | None, data: Type[BaseModel] | None) -> requests.Response:
        return self.execute(HttpMethod.PUT, schema, endpoint, params, data)

    def delete(self, schema: Type[BaseModel] | None, endpoint: str, params : dict | None, data: Type[BaseModel] | None) -> requests.Response:
        return self.execute(HttpMethod.DELETE, schema, endpoint, params, data)


    def __validation_response(schema: Type[BaseModel], response: requests.Response) -> None:
        schema.model_validate(response.json())
