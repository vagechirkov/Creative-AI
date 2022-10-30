import asyncio

from fastapi import FastAPI

from models.MessageSchema import MessageSchema
from rabbitmq.pika_client import PikaClient

from logging_conf import LOGGING
import logging.config

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('LogzioLogger')

app = FastAPI()


async def process_incoming_message(message: dict):
    logger.info(f'FastAPI: {message}')
    await asyncio.sleep(1)
    pika_client.send_message({"message": "task done"})


pika_client = PikaClient(process_incoming_message)


@app.on_event('startup')
async def startup():
    logger.info('Starting up ML Worker')
    loop = asyncio.get_running_loop()
    task = loop.create_task(pika_client.consume(loop))
    await task


@app.post('/send-result')
async def send_message(payload: MessageSchema):
    pika_client.send_message({"message": payload.message})
    return {"status": "ok"}
