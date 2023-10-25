from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.base_config import auth_backend
from app.auth.manager import get_user_manager
from app.auth.models import user
from app.database import User, get_async_session

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/all")
async def all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(user.c.email)
    result = await session.execute(query)
    return result.scalars().all()
