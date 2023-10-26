from pydantic import BaseModel
from datetime import date


class Task_schema(BaseModel):
    name: str
    description: str
    more_info: str
    begin: date
    end: date
    when_end: str
    status: str
    priority: str
    weight: int
    category: str
    users: str


class Patch_schema(BaseModel):
    task_id: int
    name: str
    description: str
    more_info: str
    begin: date
    end: date
    when_end: str
    status: str
    priority: str
    weight: int
    category: str