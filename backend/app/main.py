import logging.config

from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
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
app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


app.include_router(generate_router, prefix="/generate", tags=["Generate"])


@app.on_event('startup')
async def startup():
    logger.info('FastAPI was started')
