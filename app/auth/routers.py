from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy import select, update, delete
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
    query = select(user.c.name)
    names = await session.execute(query)
    names = names.scalars().all()
    query = select(user.c.email)
    emails = await session.execute(query)
    emails = emails.scalars().all()
    result = dict()
    for i in range(0, len(names)):
        result[names[i]] = emails[i]
    return result


@router.get("/become_super")
async def super_users(email: str, session: AsyncSession = Depends(get_async_session)):
    stmt = update(user).where(user.c.email == email).values(is_superuser=True)
    await session.execute(statement=stmt)
    await session.commit()
    return "OK"


@router.delete("/delete/{email}")
async def delete_users(email: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(user).where(user.c.email == email)
    await session.execute(statement=stmt)
    await session.commit()
    return "OK"


@router.patch("/admin_or_not_admin/{email}/{change}")
async def delete_users(email: str, change: bool, session: AsyncSession = Depends(get_async_session)):
    stmt = update(user).where(user.c.email == email).values(is_admin=change)
    await session.execute(statement=stmt)
    await session.commit()
    return "OK"
