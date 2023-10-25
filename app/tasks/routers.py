from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
# from app.files.models import File as File_model
from app.tasks.models import Task as Task_model
from app.tasks.schemas import Task_schema

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/add")
async def upload_task(schema: Task_schema, session: AsyncSession = Depends(get_async_session)):
    for i in schema.model_dump()['users'].split(' '):
        stmt = insert(Task_model).values(name=schema.model_dump()["name"],
                                         description=schema.model_dump()["description"],
                                         more_info=schema.model_dump()["more_info"],
                                         begin=schema.model_dump()["begin"],
                                         end=schema.model_dump()["end"],
                                         status=schema.model_dump()["status"],
                                         priority=schema.model_dump()["priority"],
                                         weight=schema.model_dump()["weight"],
                                         category=schema.model_dump()["category"],
                                         users=i)
        await session.execute(stmt)
        await session.commit()
    return "OK"


@router.get('/all')
async def get_file(session: AsyncSession = Depends(get_async_session)):
    query = select(Task_model)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/me")
async def upload_task(email: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Task_model).where(Task_model.users == email)
    result = await session.execute(query)
    result = result.scalars().all()
    return result
