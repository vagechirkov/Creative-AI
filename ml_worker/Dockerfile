FROM python:3.9

WORKDIR /ml_worker

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /ml_worker/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]
