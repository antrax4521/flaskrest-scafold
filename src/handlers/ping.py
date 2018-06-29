"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

from flask_restful import Resource
from src.libs.io import IO

class Ping(Resource):
    """
    Handler for /ping
    """

    def get(self):
        """
        GET /ping
        """

        return IO.response({
            'code': 200,
            'message': 'test ok',
            'data': 'pong'
        })
