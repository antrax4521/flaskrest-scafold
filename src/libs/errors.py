import re
import src.libs.logger as logger
import src.libs.commons as commons
from src.libs.io import IO

def process_error(err):
    """Parse and evaluate an error to return a standard

    Arguments:
        err {Exception} -- Error to parse

    Returns:
        flask.Response, int -- Standard response code and object
    """

    error = commons.parse_error(err)
    logger.log(error,'ERROR')

    if re.search('unique constraint', error[0]):
        return IO.response({
            'code': 409,
            'message': 'conflict',
            'data': {
                'trace': error
            }
        })

    return IO.response({
        'code': 500,
        'message': 'error',
        'data': {
            'trace': error
        }
    })
