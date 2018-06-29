"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import logging

def config_logs(app):
    """
    Config the execution logs
    """

    logs_format = """%(message)s"""

    stream = logging.StreamHandler()
    stream.setFormatter(logging.Formatter(logs_format))

    app.logger.handlers = []
    app.logger.addHandler(stream)

    app.logger.propagate = True
    app.debug = True
