"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

from src.libs.io import IO
from src.config.server import get_app

app = get_app()

@app.route('/ping', methods=['GET'])
def ping():
    return IO.response({
        'code': 200,
        'message': 'ok',
        'data': 'pong'
    })

