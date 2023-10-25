from pydantic import BaseModel
from datetime import datetime


class Task_schema(BaseModel):
    name: str
    description: str
    more_info: str
    files: int
    begin: datetime
    end: datetime
    when_end: datetime
    status: str
    priority: int
    weight: str
    category: str
    users: str
