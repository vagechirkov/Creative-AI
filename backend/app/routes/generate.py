import asyncio
import logging

from celery.result import AsyncResult
from fastapi import APIRouter

import config
from celery_worker.tasks import generate_image
from models.image_generation import GenerateImagesRequest, \
    GeneratedImagesResponse, Image

logger = logging.getLogger(__name__)

generate_router = APIRouter()


@generate_router.post("/{user_id}/")
async def post_image_query(
        user_id: str,
        generate_params: GenerateImagesRequest) -> GeneratedImagesResponse:
    params = generate_params.dict()
    # remove RequestId from params
    params.pop('requestId')
    task = generate_image.apply_async(
        kwargs=params,
        queue=config.TASK_QUEUE)

    logger.info(f"FastAPI: Task {task.id} has been created")

    # wait for task to finish
    result = await get_task_result(task.id)

    logger.info(f"FastAPI: Task {task.id} has been completed")

    return GeneratedImagesResponse(
        requestId=generate_params.requestId,
        images=[Image(url=r) for r in result],
        celery_task_id=task.id,
        user_id=user_id)


async def get_task_result(task_id):
    task_result = AsyncResult(task_id)
    while not task_result.ready():
        await asyncio.sleep(0.1)
    return task_result.result
