# Creative AI


## Local development

### Setup environment

First you need to set up three dotenv files:

`redis.env`:

    REDIS_HOST=redis
    REDIS_PORT=6379
    REDIS_CELERY_DB_INDEX=10
    REDIS_STORE_DB_INDEX=0

`rabbitmq.env`:

    RABBITMQ_DEFAULT_USER=guest
    RABBITMQ_DEFAULT_PASS=guest
    RABBITMQ_HOST=rabbitmq
    RABBITMQ_USERNAME=guest
    RABBITMQ_PASSWORD=guest
    RABBITMQ_PORT=5672

`logzio.env`:

    LOGZIO_TOKEN=YOUR_LOGZIO_TOKEN
    LOGZIO_URL=listener.logz.io


These files are used by docker-compose to set up the Docker environments.


### Docker-compose up

To start the project, run:

    docker-compose up

After starting the docker-compose, you can access the following services HTTP endpoints:

- `rabbitmq`: [http://localhost:15672](http://localhost:15672) (guest/guest)
- `fastapi` Frontend: [http://localhost:5000/](http://localhost:5000/)
- `fastapi` Swagger UI: [http://localhost:5000/docs](http://localhost:5000/docs)
- `celery.flower` Celery flower dashboard: [http://localhost:5555/dashboard](http://localhost:5555/dashboard)


Now if you open frontend in your browser, you should see the following page:

![Frontend](/Users/chirkov/Creative-AI-draft/docs/frontend.png)


### Local development Python environment

```bash

cd fastapi

python3 -m venv venv
 
source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

```

## Useful links and resources

- [Celery configuration and defaults](https://docs.celeryq.dev/en/stable/userguide/configuration.html)
- [Async Architecture with FastAPI, Celery, and RabbitMQ](https://medium.com/cuddle-ai/async-architecture-with-fastapi-celery-and-rabbitmq-c7d029030377)
- [Asynchronous Tasks with FastAPI and Celery](https://testdriven.io/blog/fastapi-and-celery/)
- [fastapi - celery - rabbitmq - redis -> Docker](https://github.com/karthikasasanka/fastapi-celery-redis-rabbitmq)
- [Running Deep Learning Algorithms as a Service](https://towardsdatascience.com/serving-deep-learning-algorithms-as-a-service-6aa610368fde)
- [FastAPI Celery, Flower and Docker](https://www.youtube.com/watch?v=mcX_4EvYka4)