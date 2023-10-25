# FastApi project
### Frontend docs: 
## .env (must be in root directory)
```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
HOST=
PORT=""
SECRET_MANAGER=""
SECRET_JWT=""
```
## Launch for local development
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
```
pip install -r .\requirements.txt
```
```
alembic revision --autogenerate
```
```
alembic upgrade head
```
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
## Launch in docker
```
nothing 
```
# http://90.156.210.55:8000/docs#/ - swagger ui (backend documentaion)
## Used technologies
#### [FastApi](https://fastapi.tiangolo.com/)
#### [FastApi Users](https://fastapi-users.github.io/fastapi-users/12.1/)
#### [Sqlalchemy](https://www.sqlalchemy.org/)
#### [Alembic](https://alembic.sqlalchemy.org/en/latest/)
#### [Pydantic](https://docs.pydantic.dev/latest/)
#### [PostgreSQL](https://www.postgresql.org/)

# API Documentation
## Publications service
### The order of requests, the body of requests see at http://90.156.210.55:8000/docs#/
#### 1. http://90.156.210.55:8000/auth/register
#### 2. http://90.156.210.55:8000/auth/jwt/login
#### 3. http://90.156.210.55:8000/users/me (with Authorization header)
## start tests
```
pytest -v -s tests/
```

