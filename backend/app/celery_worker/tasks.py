import uuid
from time import sleep
from celery.signals import setup_logging
from .celery_config import create_celery
from .ml_model import MLModel
from logging_config import LOGGING
import logging.config

from .s3_utils import upload_file


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
model = MLModel()


@celery_app.task
def generate_image(prompt: str, sleep_time: int = 5):
    sleep(sleep_time)
    image = model.generate(prompt)
    # random unique name for the image
    file_name = f'{ str(uuid.uuid4())}.png'
    image.save(file_name)
    url = upload_file(file_name)
    if url:
        return url
    else:
        return 'Error'
