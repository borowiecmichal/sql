from connection import connect


def dodaj_autora(first_name, last_name):
    sql = f"""
    INSERT INTO author (first_name, last_name) VALUES ('{first_name}','{last_name}');
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()

def add_book(title):
    sql=f"""
    INSERT INTO book (title, id_author) VALUES ('{title}', 1)
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()