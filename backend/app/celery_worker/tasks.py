from io import BytesIO
from time import sleep
from typing import List, Union

from celery.signals import setup_logging
from .celery_config import create_celery
from .style_diffusion import StyleDiffusion
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
model = StyleDiffusion()


@celery_app.task
def generate_image(prompt: str, **kwargs) -> Union[List[str], str]:
    urls = []

    images = model.generate(prompt, **kwargs)
    for i in images:
        temp_file = BytesIO()
        i.save(temp_file, format="png")
        temp_file.seek(0)
        url = upload_file(temp_file)
        urls.append(url)

    if len(urls) > 0:
        return urls
    else:
        # TODO: Handle this case
        return 'Error'
