from fastapi import FastAPI

from models.MessageSchema import MessageSchema
from rabbitmq.pika_client import PikaClient

app = FastAPI()
pika_client = PikaClient()


@app.post('/send-message')
async def send_message(payload: MessageSchema):
    pika_client.send_message({"message": payload.message})
    return {"status": "ok"}
