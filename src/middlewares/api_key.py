import os
import json
from functools import wraps
from flask import Response, request
from src.libs.io import IO

def api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request_key = request.headers.get('X-Api-Key')
        valid_key = os.environ.get('API_KEY')

        if request_key != valid_key:
            resp, code = IO.response({
                'code': 401,
                'message': 'invalid access'
            })

            return resp, code, {'Content-Type': 'application/json'}
        return func(*args, **kwargs)
    return wrapper
