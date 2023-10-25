import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
SECRET_MANAGER = os.getenv('SECRET_MANAGER')
SECRET_JWT = os.getenv('SECRET_JWT')