from time import sleep
from celery.signals import setup_logging
from .celery_config import create_celery
from logging_config import LOGGING
import logging.config


@setup_logging.connect
def configure_logger(**kwargs):
    try:
        logging.config.dictConfig(LOGGING)
        logger = logging.getLogger(__name__)
        logger.info('Starting up Celery')
        return logger

    except Exception as e:
        print(e)


celery_app = create_celery()


@celery_app.task
def generate_image(prompt: str, sleep_time: int = 5):
    sleep(sleep_time)
    return prompt[::-1]
