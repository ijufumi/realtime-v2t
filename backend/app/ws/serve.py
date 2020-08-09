import socketio

from app.logging import logger
from app.services import S3Service


sio = socketio.AsyncServer()


class Server:
    def __init__(self):
        self.s3_service = S3Service()

    @sio.event
    def connect(self, sid):
        logger.info(f"connected: ${sid}")
        sio.enter_room(sid, 'roos', 'default')

    @sio.event
    def disconnect(self, sid):
        logger.info(f"disconnected: ${sid}")
        sio.leave_room(sid, 'room', 'default')

    @sio.event
    def message(self, sid, data):
        logger.info(f"received: ${sid}:${data}")
