from pydantic import BaseModel, constr
from datetime import datetime


class RequestTaskPost(BaseModel):
    title: constr(max_length=100)
    content: str
    tags: str

class ResponseTask(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime
    tags_names: list[str]


class RequestTaskPatch(BaseModel):
    id: int
    title: constr(max_length=100)
    content: str
    tags: str