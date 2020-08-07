import asyncio
import websockets

from app.config import Config
from app.ws import Server


def run():
    server = Server()
    ws_server = websockets.serve(server.serve, Config.WS_HOST, int(Config.WS_PORT))
    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    run()
