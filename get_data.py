from connection import connect

def get_authors():
    sql="""
    SELECT first_name, last_name FROM author
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    for autor in cursor:
        print(autor)
    conn.close()

if __name__ == '__main__':
    get_authors()