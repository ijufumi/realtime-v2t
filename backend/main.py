import asyncio
import signal

from app.config import Config
from app.ws import Server
from app.logging import logger


def stop(signum, frame):
    logger.info("shutdown...")
    exit(1)


signal.signal(signal.SIGINT,  stop)


def run():
    server = Server()


if __name__ == '__main__':
    run()
