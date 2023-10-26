from typing import Optional
from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2
from pydantic import EmailStr, ConfigDict


class UserRead(schemas.BaseUser[int]):
    """Base User model."""
    id: int
    email: EmailStr
    name: str
    is_admin: bool
    is_active: bool = True
    is_superuser: bool
    is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    name: str
    is_admin: bool
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool]
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    is_admin: bool
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
