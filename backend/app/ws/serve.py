from app.logging import logger
from app.services import S3Service

from websockets.exceptions import ConnectionClosedError


class Server:
    def __init__(self):
        self.USERS = set()
        self.s3_service = S3Service()

    async def serve(self, ws, path):
        logger.info("serve start")
        try:
            async for message in ws:
                logger.info(f"received: {message}")
                if isinstance(message, str):
                    if message == "start":
                        self.register(ws)
                        # TODO: send all data
                        continue
                    elif message == "end":
                        break
                elif isinstance(message, bytes):
                    tmp_file = self.s3_service.save_to_tmp(message)
                    key = self.s3_service.upload(tmp_file)
                    result = self.s3_service.store_to_db(key)
                    # TODO: execute voice to text
                    # TODO: notify all users
                    await ws.send("Hello")
                    pass
        except ConnectionClosedError as e:
            logger.info("connection closed.", exc_info=e)
        finally:
            self.unregister(ws)
            logger.info("serve end")

    def register(self, ws):
        self.USERS.add(ws)

    def unregister(self, ws):
        self.USERS.remove(ws)
