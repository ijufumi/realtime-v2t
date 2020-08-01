from app.logging import logger

from websockets.exceptions import ConnectionClosedError


async def serve(ws, path):
    logger.info("serve start")
    try:
        async for message in ws:
            # name = await ws.recv()
            logger.info(f"received: {message}")
            greeting = f"Hello {message}!"
            await ws.send(greeting)
    except ConnectionClosedError as e:
        logger.info("connection closed.", exc_info=e)
    finally:
        logger.info("serve end")
