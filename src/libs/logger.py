"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import time
import os
import json
import logging

LOGGER = logging.getLogger('debugger')
LOGGER.setLevel(logging.DEBUG)

CHANNEL = logging.StreamHandler()
CHANNEL.setLevel(logging.DEBUG)

FORMAT = logging.Formatter('%(message)s')
CHANNEL.setFormatter(FORMAT)

LOGGER.addHandler(CHANNEL)

def log(message=None, level='DEBUG'):
    """
    Log function for debug information
    """

    millis = int(round(time.time() * 1000))
    service = os.environ.get('APPNAME')
    code = 1
    user_ip = '0.0.0.0'
    method = 'LOG'
    path = 'logger.py'
    req_time = 0

    if not message:
        body = ''
    else:
        body = json.dumps(message)

    if service != '' and service != None:
        service = service.upper()
    else:
        service = 'SERVICE'

    request_log = '%d %s %s %d %s %s %s %d %s %s' % (
        millis,
        service,
        level,
        code,
        user_ip,
        method,
        path,
        len(body),
        req_time,
        body
    )

    LOGGER.debug(request_log)