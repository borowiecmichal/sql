from connection import connect

def get_authors():
    sql="""
    SELECT * FROM author
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == '__main__':
    get_authors()