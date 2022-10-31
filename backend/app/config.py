import os

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

BROKER_CONN_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@" \
                  f"{RABBITMQ_HOST}:{RABBITMQ_PORT}"

TASK_QUEUE = os.environ.get('TASK_QUEUE', 'generate_image')

# Logs
LOGZIO_URL = os.environ.get('LOGZIO_URL')
LOGZIO_TOKEN = os.environ.get('LOGZIO_TOKEN')
