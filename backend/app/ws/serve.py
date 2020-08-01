from app.logging import logger

from websockets.exceptions import ConnectionClosedError

USERS = set()


async def serve(ws, path):
    logger.info("serve start")
    try:
        register(ws)
        async for message in ws:
            # name = await ws.recv()
            logger.info(f"received: {message}")
            greeting = f"Hello {message}!"
            await ws.send(greeting)
    except ConnectionClosedError as e:
        logger.info("connection closed.", exc_info=e)
    finally:
        unregister(ws)
        logger.info("serve end")


def register(ws):
    USERS.add(ws)


def unregister(ws):
    USERS.remove(ws)
