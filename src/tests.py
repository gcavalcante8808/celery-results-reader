from falcon import testing
from src.app import app
from src.tasks import add
from celery.result import AsyncResult

from time import sleep
import pytest
import uuid
import falcon
import os

RESULT_BACKEND_URL = os.getenv("BROKER_URL")


@pytest.fixture()
def client():
    return testing.TestClient(app)


@pytest.mark.celery(result_backend=RESULT_BACKEND_URL)
def test_retrieve_success_result_result_by_uuid(client):
    task = add.delay(1, 2)

    sleep(0.1)
    result = client.simulate_get('/results/{}'.format(task.id))

    assert result.status == falcon.HTTP_200
    assert 'state' in result.json
    assert 'task_id' in result.json
    assert 'traceback' in result.json
    assert result.json.get('state') == task.state
    assert result.json.get('task_id') == task.id
    assert result.json.get('traceback') == task.traceback
