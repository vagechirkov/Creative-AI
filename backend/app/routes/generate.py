import asyncio
import logging

from celery.result import AsyncResult
from fastapi import APIRouter
from starlette.responses import JSONResponse

import config
from celery_worker.tasks import generate_image

logger = logging.getLogger(__name__)

generate_router = APIRouter()


@generate_router.get("/{generate_query}")
async def get_image(generate_query: str):
    task = generate_image.apply_async((generate_query, 10),
                                      queue=config.TASK_QUEUE)
    logger.info(f"Task ID: {task.id}")
    result = await get_task_result(task.id)
    return JSONResponse({"task_id": task.id, "task_result": result})


@generate_router.post("/{generate_query}")
async def post_image_query(generate_query: str):
    task = generate_image.apply_async((generate_query,),
                                      queue=config.TASK_QUEUE)
    logger.info(f"Task {task.id} has been created")
    return JSONResponse({"task_id": task.id})


@generate_router.get("/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)


async def get_task_result(task_id):
    task_result = AsyncResult(task_id)
    while not task_result.ready():
        await asyncio.sleep(0.1)
    return task_result.result
