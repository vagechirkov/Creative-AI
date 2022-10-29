# Creative AI



## Docker-compose up


After starting the docker-compose, you can access the following services HTTP endpoints:

- `rabbitmq`: [http://localhost:15672](http://localhost:15672) (guest/guest)
- `fastapi` Swagger UI: [http://localhost:5000/docs](http://localhost:5000/docs)


## Local development FastAPI

```bash

cd fastapi

python3 -m venv venv
 
source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

```