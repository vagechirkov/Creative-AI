import logging.config

from fastapi import FastAPI

from logging_config import LOGGING
from routes.generate import generate_router

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('LogzioLogger')

app = FastAPI()

app.include_router(generate_router, prefix="/generate", tags=["Generate"])


@app.on_event('startup')
async def startup():
    logger.info('FastAPI was started')
