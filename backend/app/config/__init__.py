import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = str(Path(__file__).parent.parent.parent) + '/.env'
load_dotenv(dotenv_path)


class Config:
    DEBUG = bool(os.getenv('DEBUG', False))
    WS_HOST = os.getenv("WS_HOST", 'localhost')
    WS_PORT = int(os.getenv("WS_PORT", '8080'))

    AWS_KEY = os.getenv("AWS_KEY", '')
    AWS_SECRET = os.getenv("AWS_SECRET", '')
    AWS_REGION = os.getenv("AWS_REGION", '')
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", '')

    DB_HOST = os.getenv("DB_HOST", 'localhost')
    DB_PORT = int(os.getenv("DB_PORT", '3306'))
    DB_NAME = os.getenv("DB_NAME", 'v2t')
    DB_USER = os.getenv("DB_USER", 'root')
    DB_PASS = os.getenv("DB_PASS", 'password')
    MYSQL_URI = f'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'
