import pyodbc

from collections import OrderedDict


def get(*args):
    return getcursor(*args)


def getcursor(connection_string):
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It"s good to always specify
    # ENCRYPT=yes on the client side to avoid MITM attacks.
    connection = pyodbc.connect(connection_string)
    return connection.cursor()


def getone(cursor, query):
    return cursor.execute(query).fetchone()[0]


def fetchone(cursor, query):
    return cursor.execute(query).fetchone()


def fetchall(cursor, query, *args):
    return cursor.execute(query, *args).fetchall()


class Database:
    @staticmethod
    def getconnection(connection_string):
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It"s good
        # to always specify ENCRYPT=yes on the client side to avoid MITM
        # attacks.
        return pyodbc.connect(connection_string)

    @classmethod
    def getcursor(cls, dbname):
        return cls.getconnection(dbname).cursor()

    def __init__(self, dbname):
        self.cursor = self.getcursor(dbname)

    def fetchall(self, query, *params):
        self.cursor.execute(query, *params)
        columns = [column[0] for column in self.cursor.description]
        for row in self.cursor.fetchall():
            yield OrderedDict(zip(columns, row))
