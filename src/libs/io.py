"""
Standar json io for the services
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import time
import os
from flask import request


class IO:
    """
    IO custom class
    """

    @staticmethod
    def response(data={}):
        """
        Create standarized response object
        """

        code = data['code'] if 'code' in data else 200
        status = 'success' if 200 <= code <= 202 else 'error'
        message = data['message'] if 'message' in data else ''
        service = data['object'] if 'object' in data else os.environ.get('APPNAME')
        route = request.path

        info = {
            "object": service,
            "code": code,
            "status": status,
            "message": message,
            "request": int(time.time()),
            "url": route
        }

        if 'data' in data:
            info['data'] = data['data']

        return info, code
