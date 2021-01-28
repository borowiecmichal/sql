import psycopg2
from create_query_sql import creation_query_list

data = {
    'user': 'postgres',
    'password': 'coderslab',
    'port': 5432,
    'host': 'localhost',
    'dbname': 'biblioteka'
}


def connect(connection_data=None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection


if __name__ == '__main__':
    connection = connect()
    connection.close()
