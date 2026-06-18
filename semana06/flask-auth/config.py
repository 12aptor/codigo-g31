import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)