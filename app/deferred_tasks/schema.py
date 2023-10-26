from typing import List

from pydantic import BaseModel, EmailStr


class EmailSchemaAdmin(BaseModel):
    email: List[EmailStr]


class EmailSchemaTask(BaseModel):
    email: List[EmailStr]
    name_task: str

class TestSchema(BaseModel):
    email: EmailStr


