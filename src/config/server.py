"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import time
import os
import json
from flask import Flask, request, g
from flask_restful import Api
from werkzeug.serving import WSGIRequestHandler
from src.config.logs import config_logs
from src.config.routes import create_routes
from src.monkeypatch.request_logs import werk_log

"""
App register section
"""
APP = Flask(__name__)
API = Api(APP)

config_logs(APP)
create_routes(API)

"""
Patch section
"""
WSGIRequestHandler.log = werk_log

"""
Hooks for the flask core
"""

@APP.before_request
def before_request():
    """
    Execute this code before the request execution
    """

    g.request_start_time = time.time()
    g.request_time = lambda: "%f" % (time.time() - g.request_start_time)


@APP.after_request
def after_request(response):
    """
    Execute this code after the request execution
    """

    millis = int(round(time.time() * 1000))
    service = os.environ.get('APPNAME')
    code = response.status_code
    user_ip = request.remote_addr
    method = request.method.upper()
    path = request.path
    req_time = g.request_time()

    if path == '/ping':
        return response

    if not request.data:
        body = ''
    else:
        body = json.dumps(request.get_json())

    if service != '' and service != None:
        service = service.upper()
    else:
        service = 'SERVICE'

    headers = {}
    for header in request.headers:
        headers[header[0]] = header[1]

    data = {
        'headers': headers,
        'body': body
    }

    request_log = '%d %s REQUEST %d %s %s %s %d %s %s' % (
        millis,
        service,
        code,
        user_ip,
        method,
        path,
        len(body),
        req_time,
        json.dumps(data)
    )

    APP.logger.debug(request_log)

    return response
