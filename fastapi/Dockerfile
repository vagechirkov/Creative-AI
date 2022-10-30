FROM python:3.9

WORKDIR /fastapi

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /fastapi/app

ENV PORT 5000

# Sleep 10 seconds to wait for the RabbitMQ container to be ready
# SEE also: https://docs.docker.com/compose/startup-order/
CMD sleep 10 && uvicorn main:app --host 0.0.0.0 --port $PORT --reload