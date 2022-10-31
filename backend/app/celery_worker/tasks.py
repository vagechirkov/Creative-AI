from .worker import celery
from time import sleep


@celery.task
def generate_image(prompt: str):
    sleep(5)
    return prompt[::-1]
