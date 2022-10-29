import asyncio

from fastapi import FastAPI

from models.MessageSchema import MessageSchema
from rabbitmq.pika_client import PikaClient

app = FastAPI()


def process_incoming_message(message):
    print(message)


pika_client = PikaClient(process_incoming_message)


@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(pika_client.consume(loop))
    await task


@app.post('/send-task')
async def send_message(payload: MessageSchema):
    pika_client.send_message({"message": payload.message})
    return {"status": "ok"}
