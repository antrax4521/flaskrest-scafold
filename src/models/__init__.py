"""
Import all your models here
"""

from src.config.server import get_database

db = get_database()
db.generate_mapping(create_tables=False)