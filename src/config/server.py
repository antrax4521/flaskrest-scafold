"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import time
import os
import json
import psycopg2
from flask import Flask, request, g, Response
from werkzeug.serving import WSGIRequestHandler
from src.config.logs import config_logs
from src.config.database import get_database
from src.monkeypatch.request_logs import werk_log
from flask_jsonschema import JsonSchema, ValidationError
from flask_cors import CORS
from src.libs.io import IO
import src.libs.logger as logger
import src.libs.commons as commons

"""
App register section
"""
APP = Flask(__name__)
CORS(APP)

config_logs(APP)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

APP.config['JSONSCHEMA_DIR'] = DIR_PATH + '/../schemas'

JSON_SCHEMA = JsonSchema(APP)

DB = get_database()

"""
Patch section
"""
WSGIRequestHandler.log = werk_log


"""
Hooks for the flask core
"""

@APP.errorhandler(psycopg2.IntegrityError)
def integrity_error(e):
    logger.log({'error': str(e)})

    return IO.response({
        'code': 409,
        'message': 'integrity error',
        'data': {
            'trace': commons.parse_error(e)
        }
    })

@APP.errorhandler(ValidationError)
def on_validation_error(e):
    logger.log({'error': str(e)}, 'ERROR')

    return IO.response({
        'code': 422,
        'message': 'unprosesable data',
        'data': {
            'trace': commons.parse_error(e)
        }
    })

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


"""
Functions that returns configuration objects
"""

def get_app():
    return APP

def get_jsonschema():
    return JSON_SCHEMA

def get_database():
    return DB
