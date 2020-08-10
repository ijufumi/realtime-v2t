import socketio
from sanic import Sanic

from app.config import Config
from app.logging import logger
from app.services import S3Service


sio = socketio.AsyncServer(async_mode='sanic')
app = Sanic()
sio.attach(app)


class Server:
    def __init__(self):
        self.s3_service = S3Service()

    @sio.on("connect", namespace="room")
    def connect(self, sid):
        logger.info(f"connected: ${sid}")
        sio.enter_room(sid, 'roos', 'default')

    @sio.on("disconnect", namespace="room")
    def disconnect(self, sid):
        logger.info(f"disconnected: ${sid}")
        sio.leave_room(sid, 'room', 'default')

    @sio.on("message", namespace="room")
    def message(self, sid, data):
        logger.info(f"received: ${sid}:${data}")

    @staticmethod
    def run():
        app.run(host=Config.WS_HOST, port=Config.WS_PORT)
