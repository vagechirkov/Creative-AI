import json
import uuid

import pika as pika
from envparse import env


class PikaClient:
    def __init__(self):
        self.publish_queue_name = env('PUBLISH_QUEUE', 'noname_publish_queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=env('RABBIT_HOST', '127.0.0.1'))
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(
            queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None

    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )
