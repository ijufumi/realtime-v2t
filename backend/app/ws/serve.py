import socketio
import eventlet
from typing import Text, List

from app.config import Config
from app.logging import logger
from app.services import S3Service, GoogleSpeechService


manager = socketio.BaseManager()
sio = socketio.Server(async_mode='eventlet', client_manager=manager, binary=True, cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

s3_service = S3Service()
speech_service = GoogleSpeechService()


@sio.event
def connect(sid: Text, environ) -> None:
    logger.info(f"connected: {sid}")
    data = s3_service.get_all_from_db()
    for d in data:
        url = s3_service.get_pre_signed_url(d.key)
        sio.emit("send_result", {"id": d.id, "url": url, "texts": d.text})


@sio.event
def disconnect(sid) -> None:
    logger.info(f"disconnected: {sid}")


@sio.event
def voice_message(sid: Text, data: List[bytes]) -> None:
    logger.info(f"[{sid}]received voice message")
    file_path = s3_service.save_to_tmp(data)
    file_path = s3_service.convert(file_path)
    key = s3_service.upload(file_path)
    result = s3_service.store_to_db(key)
    url = s3_service.get_pre_signed_url(key)
    texts = speech_service.to_text(str(file_path.resolve()))
    logger.info(f"[{sid}] result:{texts}")
    result.text = texts
    s3_service.save(result)
    sio.emit("send_result", {"id": result.id, "url": url, "texts": texts})


@sio.event
def message(sid: Text, data: Text) -> None:
    logger.info(f"[{sid}]received message:{data}")


def run_server():
    eventlet.wsgi.server(eventlet.listen(('', Config.WS_PORT)), app, log=logger)
