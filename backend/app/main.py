from fastapi import FastAPI

from logging_conf import LOGGING
import logging.config

from routes.generate import generate_router

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('LogzioLogger')

app = FastAPI()

app.include_router(generate_router, prefix="/generate", tags=["Generate"])
