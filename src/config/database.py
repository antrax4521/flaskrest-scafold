import os
from pony.orm import Database

def parse_connection_string(con):
    """
    Format a standard postgres URL to specific connection string to be used
    in pyscopg2
    :param con: str
    :return: str
    """

    con = con.replace('postgres://', '')

    parts = con.split('@')

    if len(parts) == 2:
        # user => parts[0][0]
        # pass => parts[0][1]
        # host => parts[1][0][0]
        # port => parts[1][0][1]
        # dbas => parts[1][1]

        parts[0] = parts[0].split(':')

        if len(parts[0]) < 1:
            raise Exception('Invalid connection string')
        elif len(parts[0]) == 1:
            parts[0][1] = ''

        parts[1] = parts[1].split('/')

        if len(parts[1]) != 2:
            raise Exception('Invalid connection string')

        parts[1][0] = parts[1][0].split(':')
    else:
        raise Exception('Invalid connection string')

    return parts[1][1], parts[0][0], parts[1][0][0], parts[1][0][1], parts[0][1]


DBAS, USER, HOST, PORT, PASS = parse_connection_string(os.environ.get('DATABASE_URL'))

DB = Database()
DB.bind(provider='postgres', database=DBAS, user=USER, password=PASS, host=HOST, port=PORT)


def get_database():
    return DB
