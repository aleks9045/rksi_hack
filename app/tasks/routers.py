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
    for i in schema.dict()['users'].split(' '):
        stmt = insert(Task_model).values(name=schema.dict()["name"],
                                         description=schema.dict()["description"],
                                         more_info=schema.dict()["more_info"],
                                         # files=schema.dict()["files"],
                                         begin=schema.dict()["begin"],
                                         end=schema.dict()["end"],
                                         status=schema.dict()["status"],
                                         when_end=schema.dict()["when_end"],
                                         priority=schema.dict()["priority"],
                                         weight=schema.dict()["weight"],
                                         category=schema.dict()["category"],
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
    print(result)
    return result
