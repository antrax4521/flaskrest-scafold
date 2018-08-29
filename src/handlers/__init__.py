"""
Import all your handler files here
"""

import src.handlers.ping
import src.libs.commons as commons
import src.libs.logger as logger
from src.config.server import get_app
from flask_jsonschema import ValidationError
from src.libs.io import IO
from psycopg2 import IntegrityError
from werkzeug.exceptions import (
    BadRequest,
    NotFound,
    InternalServerError
)

app = get_app()

@app.errorhandler(IntegrityError)
def integrity_error(e):
    error = commons.parse_error(e)

    return IO.response({
        'code': 409,
        'message': 'integrity error',
        'data': {
            'trace': error
        }
    })

@app.errorhandler(ValidationError)
def validation_error(e):
    error = commons.parse_error(e)

    return IO.response({
        'code': 422,
        'message': 'unprosesable data',
        'data': {
            'trace': error
        }
    })

@app.errorhandler(BadRequest)
def bad_request(ex):
    error = commons.parse_error(ex)

    return IO.response({
        'code': 400,
        'message': 'bad request',
        'data': {
            'trace': error
        }
    })

@app.errorhandler(NotFound)
def not_fount(ex):
    error = commons.parse_error(ex)

    return IO.response({
        'code': 404,
        'message': 'not found',
        'data': {
            'trace': error
        }
    })

@app.errorhandler(InternalServerError)
@app.errorhandler(Exception)
def internal_server_error(ex):
    error = commons.parse_error(ex)

    return IO.response({
        'code': 500,
        'message': 'internal server errort',
        'data': {
            'trace': error
        }
    })

