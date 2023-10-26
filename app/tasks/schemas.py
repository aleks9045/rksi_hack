from pydantic import BaseModel
from datetime import date


class Task_schema(BaseModel):
    name: str
    description: str
    more_info: str
    begin: date
    end: date
    when_end: str = "Popa"
    status: str
    priority: str
    weight: int
    category: str
    users: str
