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


@sio.event
def disconnect(sid) -> None:
    logger.info(f"disconnected: {sid}")


@sio.event
def voice_message(sid: Text, data: bytes) -> None:
    logger.info(f"received voice message:{sid}")
    file_path = s3_service.save_to_tmp(data)
    key = s3_service.upload(file_path)
    s3_service.store_to_db(key)
    url = s3_service.get_pre_signed_url(key)
    sio.emit("send_result", {"key": key, "url": url})


def run_server():
    eventlet.wsgi.server(eventlet.listen(('', Config.WS_PORT)), app, log=logger)
