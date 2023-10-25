import aiofiles
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.files.models import File as File_model

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post('/add')
async def upload_file(task: int, files: list[UploadFile], session: AsyncSession = Depends(get_async_session)):
    for file in files:
        file_path = f'static/{file.filename}'
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = file.file.read()
            await out_file.write(content)
        stmt = insert(File_model).values(file_name=file.filename, file_path=file_path)
        await session.execute(statement=stmt)
        await session.commit()
    return {"status": "files was saved"}


@router.get('/get')
async def get_file(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(File_model.file_path).where(File_model.id == id)
    result = await session.execute(query)
    file_path = result.scalars().all()[0]
    return "http://90.156.210.55:8000/" + file_path


@router.get('/all')
async def get_file(session: AsyncSession = Depends(get_async_session)):
    query = select(File_model)
    result = await session.execute(query)
    return result.scalars().all()
