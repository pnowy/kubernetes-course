import time

from flask import Flask
from flask import request
import os

app = Flask(__name__)
start_time = time.time()
startup_probe_passed = False


@app.route('/pods/env-var')
def get_env_variable():
    env_name = request.args.get('variable')
    if env_name in os.environ:
        return f"Hello {os.environ[env_name]}!"
    else:
        return "Hello anonymous!"


@app.route('/pods/env-vars')
def get_env_variables():
    return dict(os.environ)


@app.route('/api/features')
def get_features():
    return {
        "hostname": os.environ["HOSTNAME"],
        "feature-a": "available",
        "feature-b": "available",
        # "feature-c": "available",
    }


@app.route('/hostname')
def get_host_name():
    if "HOSTNAME" in os.environ:
        return {"HOSTNAME": os.environ["HOSTNAME"]}
    else:
        return "Missing hostname"


@app.route('/health/liveness')
def get_health_liveness():
    response_status = request.args.get('status', 200)
    response_delay = request.args.get('delay', 0.2, type=float)
    print(f"Liveness probe requested, status: {response_status}, delay: {response_delay}")
    time.sleep(response_delay)
    return {
        "endpoint": "liveness",
        "status": response_status,
        "delay": response_delay
    }, response_status


@app.route('/health/readiness')
def get_health_readiness():
    response_status = request.args.get('status', 200)
    response_delay = request.args.get('delay', 0.4, type=float)
    print(f"Readiness probe requested, status: {response_status}, delay: {response_delay}")
    time.sleep(response_delay)
    return {
        "endpoint": "readiness",
        "status": response_status,
        "delay": response_delay
    }, response_status


@app.route('/health/startup')
def get_health_startup():
    seconds_from_start = int(time.time() - start_time)
    response_status = 200 if seconds_from_start > 60 else 400
    print(f"Startup probe requested, status: {response_status}, seconds_from_start: {seconds_from_start}")
    return {
        "endpoint": "startup",
        "status": response_status,
        "seconds_from_start": seconds_from_start
    }, response_status


@app.route('/')
def index():
    return "Hello in Kubernetes course!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
