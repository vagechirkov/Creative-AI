import logging.config
from typing import Any

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette_exporter import PrometheusMiddleware, handle_metrics

from logging_config import LOGGING
from routes.generate import generate_router

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

app = FastAPI()

# metrics on the /metrics endpoint for prometheus
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def https_url_for(request: Request, name: str, **path_params: Any) -> str:
    http_url = request.url_for(name, **path_params)

    # Replace 'http' with 'https'
    return http_url.replace("http", "https", 1)


templates.env.globals["https_url_for"] = https_url_for


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


app.include_router(generate_router, prefix="/generate", tags=["Generate"])


@app.on_event('startup')
async def startup():
    logger.info('FastAPI was started')
