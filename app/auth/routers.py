from fastapi_users import FastAPIUsers
import aiofiles
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.base_config import auth_backend
from app.auth.manager import get_user_manager
from fastapi import APIRouter, UploadFile, File, Depends

from app.auth.models import user
from app.database import User, get_async_session

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

photo_router = APIRouter(
    prefix="/photo",
    tags=["Photo"]
)


@photo_router.post('/add')
async def upload_photo(file: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)):
    file_path = f'app/static/{file.filename}'
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write