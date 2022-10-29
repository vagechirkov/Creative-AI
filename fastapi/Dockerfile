FROM python:3.9

WORKDIR /fastapi

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /fastapi/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
