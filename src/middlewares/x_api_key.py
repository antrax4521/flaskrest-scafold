"""
Author: Eudardo Aguilar <dante.aguilar41@gmail.com>
"""

import os
import json
from functools import wraps
from flask import Response, request
from src.libs.io import IO

def x_api_key(func):
    """
    Decorator middleware that validate the x-api-key header
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper for the middleware and main logic
        """

        request_key = request.headers.get('X-Api-Key')
        valid_key = os.environ.get('API_KEY')

        if request_key != valid_key:
            resp, code = IO.response({
                'code': 401,
                'message': 'invalid access'
            })

            return Response(json.dumps(resp), code, {'Content-Type': 'application/json'})

        return func(*args, **kwargs)

    return wrapper
