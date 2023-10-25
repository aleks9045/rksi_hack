from pydantic import BaseModel
from datetime import datetime


class Task_schema(BaseModel):
    name: str
    description: str
    more_info: str
    begin: datetime
    end: datetime
    status: str
    priority: str
    weight: int
    category: str
    users: str
