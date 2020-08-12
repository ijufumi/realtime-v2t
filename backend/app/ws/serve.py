import socketio
from typing import Text, Dict, Any
from sanic import Sanic
from sanic_cors import CORS

from app.config import Config
from app.logging import logger
from app.services import S3Service


manager = socketio.BaseManager()
sio = socketio.Server(client_manager=manager, binary=True, cors_allowed_origins=[])
sio.binary = True
app = Sanic()
app.config['CORS_AUTOMATIC_OPTIONS'] = True
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
CORS(app)
#sio.attach(app)


class Server:
    def __init__(self):
        self.s3_service = S3Service()

    @sio.on("connect")
    async def connect(self, sid: Text) -> None:
        logger.info(f"connected: {sid}")
        #sio.enter_room(sid, 'roos', 'default')

    @sio.on("disconnect")
    async def disconnect(self, sid: Text) -> None:
        logger.info(f"disconnected: {sid}")
        #sio.leave_room(sid, 'room', 'default')

    @sio.event
    async def message(self, sid: Text, data: Any) -> None:
        logger.info(f"received: {sid}:{data}")

    @staticmethod
    def run():
        app.run(host=Config.WS_HOST, port=Config.WS_PORT)

