from celery import current_app as current_celery_app
from kombu import Queue

import config


def create_celery():
    celery_app = current_celery_app
    celery_app.conf.update(
        broker_url=config.BROKER_CONN_URI,
        # result_backend=config.BACKEND_CONN_URI,
        task_serializer='json',
        accept_content=['json'],  # Ignore other content
        result_serializer='json',
        timezone='Europe/Berlin',
        enable_utc=True,
        current_task_queues=[Queue("celery"), Queue(config.TASK_QUEUE)],
    )
    return celery_app
