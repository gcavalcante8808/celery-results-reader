import json
import os
from celery import Celery
from falcon import API
from werkzeug.serving import run_simple
from celery.result import ResultBase, AsyncResult
from celery.backends.redis import RedisBackend


RESULT_BACKEND_URL = os.getenv('RESULT_BACKEND_URL')
BROKER_URL = os.getenv('BROKER_URL')


#From: https://github.com/falconry/falcon/issues/1220
class HandleCORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')


class AsyncResultResource:
    def __init__(self):
        self.celeryapp = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND_URL)

    def on_get(self, req, resp, task_id):
        result = AsyncResult(task_id, backend=self.celeryapp.backend)
        resp.body = json.dumps(
            {'task_id': task_id,
             'state': result.state,
             'traceback': result.traceback}
        )


app = API(middleware=HandleCORSMiddleware())
app.add_route('/results/{task_id}', AsyncResultResource())

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
