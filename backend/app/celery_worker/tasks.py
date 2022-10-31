from time import sleep
from celery.signals import setup_logging
from .celery_config import create_celery
from logging_config import LOGGING
import logging.config


@setup_logging.connect
def configure_logger(**kwargs):
    try:
        logging.config.dictConfig(LOGGING)
        logger = logging.getLogger('LogzioLogger')
        logger.info('Starting up Celery')
        return logger

    except Exception as e:
        print(e)


celery_app = create_celery()


@celery_app.task
def generate_image(prompt: str):
    sleep(5)
    return prompt[::-1]
