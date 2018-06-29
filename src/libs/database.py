"""
Author: Eduardo Aguilar <dante.aguilar41@gmail.com>
"""

import os
import psycopg2
from psycopg2 import ProgrammingError


class Database:
    """
    Database Conections for the proyect
    """

    def __init__(self, autocommit=False):
        """
        Database connections init
        """

        str_connection = self._parse_connection_string(
            os.environ.get('DATABASE_URL')
        )

        self.conx = psycopg2.connect(str_connection)

        if autocommit:
            self.conx.autocommit = True

        self.cur = self.conx.cursor()

    @staticmethod
    def _parse_connection_string(con):
        """
        Format a standard postgres URL to specific connection string to be used
        in pyscopg2
        :param con: str
        :return: str
        """

        str_connection = "dbname='%s' user='%s' host='%s' password='%s'"

        con = con.replace('postgres://', '')

        parts = con.split('@')

        if len(parts) == 2:
            # user => parts[0][0]
            # pass => parts[0][1]
            # host => parts[1][0]
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
            parts[1][0] = parts[1][0][0]
        else:
            raise Exception('Invalid connection string')

        return str_connection % (parts[1][1], parts[0][0], parts[1][0], parts[0][1])

    def commit(self):
        """
        Commit all query transactions
        """

        self.conx.commit()
