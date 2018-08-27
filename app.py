"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import os
import src.handlers
from src.config.server import APP

app = APP

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    APP.run(host="0.0.0.0", port=PORT, debug=True)
