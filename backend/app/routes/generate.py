import logging

from fastapi import APIRouter
from starlette.responses import JSONResponse

import config
from celery_worker.tasks import generate_image

logger = logging.getLogger(__name__)

generate_router = APIRouter()


@generate_router.get("/{generate_query}")
async def generate_image_query(generate_query: str):
    task = generate_image.apply_async((generate_query,))
    logger.info(f"Task {task.id} has been created")
    return JSONResponse({"task_id": task.id})
