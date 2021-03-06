import socketio
import eventlet
from typing import Text, List

from app.config import Config
from app.logging import logger
from app.services import S3Service, GoogleSpeechService


manager = socketio.BaseManager()
sio = socketio.Server(async_mode='eventlet', client_manager=manager, binary=True, cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={'/static': './app/ws/static/index.html'})

s3_service = S3Service()
speech_service = GoogleSpeechService()


@sio.event
def connect(sid: Text, environ) -> None:
    logger.info(f"[{sid}]connected")
    send_all()

@sio.event
def disconnect(sid) -> None:
    logger.info(f"[{sid}]disconnected")


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


@sio.event
def delete_result(sid: Text, result_id: Text) -> None:
    logger.info(f"[{sid}]received delete message:{result_id}")
    s3_service.delete(result_id)
    send_all()


def send_all():
    data = s3_service.get_all_from_db()
    logger.info(f"data size is {len(data)}")
    results = []
    for d in data:
        url = s3_service.get_pre_signed_url(d.audio_key)
        results.append({"id": d.id, "url": url, "texts": d.text})

    sio.emit("send_results", results)


def run_server():
    eventlet.wsgi.server(eventlet.listen(('', Config.WS_PORT)), app, log=logger)
