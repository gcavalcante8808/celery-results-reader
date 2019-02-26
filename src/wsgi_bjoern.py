import os
import signal

import bjoern

from src.app import app

NUM_WORKERS = 8
worker_pids = []

bjoern.listen(app, '0.0.0.0', 8000)
for _ in range(NUM_WORKERS):
    pid = os.fork()
    if pid > 0:
        worker_pids.append(pid)
    elif pid == 0:
        try:
            bjoern.run()
        except KeyboardInterrupt:
            pass
        exit()
try:
    pid, xx = os.wait()
    worker_pids.remove(pid)
finally:
    for pid in worker_pids:
        os.kill(pid, signal.SIGINT)
        exit(1)
