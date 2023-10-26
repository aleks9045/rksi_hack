from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.files.models import File as File_model
from app.tasks.models import Task as Task_model
from app.tasks.schemas import Task_schema, Patch_schema

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/add")
async def upload_task(schema: Task_schema, session: AsyncSession = Depends(get_async_session)):
    ids_lst = []
    count = -1
    for j, i in enumerate(schema.model_dump()['users'].split(' ')):
        stmt = insert(Task_model).values(name=schema.model_dump()["name"],
                                         description=schema.model_dump()["description"],
                                         more_info=schema.model_dump()["more_info"],
                                         begin=schema.model_dump()["begin"],
                                         end=schema.model_dump()["end"],
                                         when_end=schema.model_dump()["when_end"],
                                         status=schema.model_dump()["status"],
                                         priority=schema.model_dump()["priority"],
                                         weight=schema.model_dump()["weight"],
                                         category=schema.model_dump()["category"],
                                         users=i)
        await session.execute(stmt)
        await session.commit()
        count += 1

    query = select(Task_model.id).where(Task_model.name == schema.model_dump()["name"])
    result = await session.execute(query)
    max_id = max(result.scalars().all())
    ids_lst.append(max_id)
    # ids_lst.append(max_id - i for i in)
    while count != 0:
        max_id -= 1
        ids_lst.append(max_id)
        count -= 1
    return ids_lst


@router.get('/all')
async def all_task(session: AsyncSession = Depends(get_async_session)):
    query = select(Task_model)
    result = await session.execute(query)
    result_data = result.scalars().all()

    query = select(Task_model.id)
    result = await session.execute(query)
    result_ids = result.scalars().all()

    ids_dct = {}
    for i in result_ids:
        query = select(File_model.file_path).where(File_model.task == i)
        result = await session.execute(query)
        ids_dct[i] = result.scalars().all()

    return {"data": result_data, "files": ids_dct}


@router.get("/me")
async def my_tasks(email: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Task_model).where(Task_model.users == email)
    result = await session.execute(query)
    result_data = result.scalars().all()

    query = select(Task_model.id).where(Task_model.users == email)
    result = await session.execute(query)
    result_ids = result.scalars().all()

    ids_dct = {}
    for i in result_ids:
        query = select(File_model.file_path).where(File_model.task == i)
        result = await session.execute(query)
        ids_dct[i] = result.scalars().all()

    return {"data": result_data, "files": ids_dct}


@router.patch("/patch")
async def patch_task(schema: Patch_schema, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Task_model).where(Task_model.id == schema.model_dump()["task_id"]) \
        .values(name=schema.model_dump()["name"],
                description=schema.model_dump()["description"],
                more_info=schema.model_dump()["more_info"],
                begin=schema.model_dump()["begin"],
                end=schema.model_dump()["end"],
                when_end=schema.model_dump()["when_end"],
                status=schema.model_dump()["status"],
                priority=schema.model_dump()["priority"],
                weight=schema.model_dump()["weight"],
                category=schema.model_dump()["category"]
                )
    await session.execute(stmt)
    await session.commit()
    return "OK"


@router.delete("/delete")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Task_model).where(Task_model.id == task_id)
    await session.execute(stmt)
    await session.commit()
    return "OK"
