import sqlite3

db_type = ''
connection_string = ''


def init(env: dict):
    global db_type, connection_string
    db_type = env['DB_TYPE']
    connection_string = env['DB_CONNECTION_STRING']


def execute(query: str) -> tuple:
    global db_type, connection_string
    if db_type == 'sqlite':
        conn = sqlite3.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return tuple(result)
    else:
        raise UnsupportedDatabaseError(db_type)


class UnsupportedDatabaseError(Exception):
    def __init__(self, db_name: str):
        super().__init__(f'Unsupported database: {db_name}')
