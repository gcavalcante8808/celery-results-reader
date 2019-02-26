from celery import Celery
import os

RESULT_BACKEND_URL = os.getenv('RESULT_BACKEND_URL')
BROKER_URL = os.getenv("BROKER_URL")

app = Celery('src.tasks', broker=BROKER_URL, backend=RESULT_BACKEND_URL)


@app.task(name='src.tasks.add')
def add(x, y):
    return x + y
