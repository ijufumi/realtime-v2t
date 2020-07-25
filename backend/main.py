import asyncio
import websockets

from app.config import Config
from app.ws import serve


def run():
    ws_server = websockets.serve(serve, Config.WS_HOST, int(Config.WS_PORT))
    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forver()


if __name__ == '__main__':
    run()
