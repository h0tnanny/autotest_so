from typing import Any, Dict
from pydantic import BaseModel
from requests import Response


class ResponseData(BaseModel):
    data_response: Response
    data_json: str | None
