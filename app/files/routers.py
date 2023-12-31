import aiofiles
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.files.models import File as File_model
from app.tasks.models import Task as Task_model


router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post('/add')
async def upload_file(task_id: str, file: UploadFile, session: AsyncSession = Depends(get_async_session)):
    for id in task_id.split(' '):
        file_path = f'static/{file.filename}'
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = file.file.read()
            await out_file.write(content)
        stmt = insert(File_model).values(task=int(id), file_name=file.filename, file_path=file_path)
        await session.execute(statement=stmt)
        await session.commit()
    return {"status": "files was saved"}


@router.get('/all')
async def all_file(session: AsyncSession = Depends(get_async_session)):
    query = select(File_model)
    result = await session.execute(query)
    return result.scalars().all()
