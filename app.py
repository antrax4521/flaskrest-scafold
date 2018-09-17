"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import os
import src.handlers
from src.config.server import get_app

app = get_app()

if __name__ == '__main__':
    port = os.environ.get('PORT')
    port = 5000 if not port else int(port)

    app.run(host="0.0.0.0", port=port, debug=True)


