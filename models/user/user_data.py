from pydantic import BaseModel


class UserData(BaseModel):
    id: str
    first_name: str
    last_name: str
    middle_name: str
