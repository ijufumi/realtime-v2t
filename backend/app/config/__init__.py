import os


class Config:
    WS_HOST = os.getenv("WS_HOST", 'localhost')
    WS_PORT = os.getenv("WS_PORT", '8080')
