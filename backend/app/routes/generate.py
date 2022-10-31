from fastapi import APIRouter

import config
from celery_worker.tasks import generate_image


generate_router = APIRouter()


@generate_router.get("/{generate_query}")
async def generate_image_query(generate_query: str):
    generate_image.apply_async((generate_query,))  # , queue=config.TASK_QUEUE
    return True
