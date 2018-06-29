"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

from src.handlers.ping import Ping

def create_routes(api):
    """
    Register al API routes
    """

    api.add_resource(Ping, '/ping')
