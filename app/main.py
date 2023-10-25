from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.auth.routers import fastapi_users, auth_backend, router as user_router
from app.auth.schemas import UserRead, UserCreate, UserUpdate
from app.files.routers import router as file_router
from app.tasks.routers import router as task_router
from app.deferred_tasks.routers import router as deferred_router

app = FastAPI(title="Swagger UI")

origins = [
    "http://localhost",
    "http://90.156.210.55",
    "*"
]  # Сервера, которые могут отправлять запросы на Backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Access-Control-Allow-Origin",
                   "Access-Control-Allow-Methods", "X-Requested-With",
                   "Authorization", "X-CSRF-Token"]
)  # Побеждаем политику CORS

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    file_router
)

app.include_router(
    task_router
)

app.include_router(
    user_router
)

app.include_router(
    deferred_router
)

app.mount("/static", StaticFiles(directory="static"), name="static")
