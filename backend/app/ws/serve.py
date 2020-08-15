import socketio
import eventlet
from typing import Text, Dict, Any

from app.config import Config
from app.logging import logger
from app.services import S3Service


manager = socketio.BaseManager()
sio = socketio.Server(async_mode='eventlet', client_manager=manager, binary=True, cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

s3_service = S3Service()


@sio.event
def connect(sid: Text, environ) -> None:
    logger.info(f"connected: {sid}")
    #sio.enter_room(sid, 'roos', 'default')


@sio.event
def disconnect(sid) -> None:
    logger.info(f"disconnected: {sid}")
    #sio.leave_room(sid, 'room', 'default')


@sio.event
def message(sid: Text, data: Any) -> None:
    logger.info(f"received: {sid}:{data}")


def run_server():
    eventlet.wsgi.server(eventlet.listen(('', Config.WS_PORT)), app, log=logger)
