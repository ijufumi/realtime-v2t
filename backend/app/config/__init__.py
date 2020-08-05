import os


class Config:
    WS_HOST = os.getenv("WS_HOST", 'localhost')
    WS_PORT = os.getenv("WS_PORT", '8080')

    AWS_KEY = os.getenv("AWS_KEY", '')
    AWS_SECRET = os.getenv("AWS_SECRET", '')
    AWS_REGION = os.getenv("AWS_REGION", '')
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", '')

    DB_HOST = os.getenv("DB_HOST", '')
    DB_PORT = os.getenv("DB_PORT", '')
    DB_NAME = os.getenv("DB_NAME", '')
    DB_USER = os.getenv("DB_USER", '')
    DB_PASS = os.getenv("DB_PASS", '')
    MYSQL_URI = f'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
