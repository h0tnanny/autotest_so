from pydantic import BaseModel


class PageInfo(BaseModel):
    page_from: int = 0
    page_size: int = 0
