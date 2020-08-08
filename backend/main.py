import asyncio
import websockets
import signal
from websockets.http import Headers

from app.config import Config
from app.ws import Server
from app.logging import logger

CORS_HEADERS = Headers([("Access-Control-Allow-Origin", "*")])


def stop(signum, frame):
    logger.info("shutdown...")
    exit(1)


signal.signal(signal.SIGINT,  stop)


def run():
    server = Server()
    ws_server = websockets.serve(server.serve, Config.WS_HOST, int(Config.WS_PORT), origins=["*"])
    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    run()
