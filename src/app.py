import json

from falcon import API
from werkzeug.serving import run_simple
from celery.result import ResultBase, AsyncResult


class AsyncResultResource:
    def on_get(self, req, resp, task_id):
        result = AsyncResult(task_id)
        resp.body = json.dumps(
            {'task_id': task_id,
             'state': result.state,
             'traceback': result.traceback}
        )


app = API()
app.add_route('/results/{task_id}', AsyncResultResource())

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
