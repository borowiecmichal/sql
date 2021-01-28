import psycopg2

data = {
    'user': 'postgres',
    'password': 'coderslab',
    'port': 5432,
    'host': 'localhost',
    'dbname': 'exercises_db'
}

connection = psycopg2.connect(**data)
connection.autocommit = True
cursor = connection.cursor()

while True:
    while True:
        try:
            choice = int(input("Wybierz opcję:\n1 - Wyświetl produkty\n2 - Dodaj produkt\n3 - wyłącz program\nWybór: "))
            if choice == 1 or choice == 2 or choice == 3:
                break
        except:
            continue

    if choice == 1:
        query = """
        SELECT * FROM products
        order by price desc ;
        """
        cursor.execute(query)
        for row in cursor:
            print(row)

    if choice == 2:
        name = input('Podaj nazwe: ')
        descr = input("Podaj opis: ")
        while True:
            try:
                price = float(input("Podaj cene: "))
                break
            except:
                print('Podaj cene w dobrym formacie')
                continue
        query = f"INSERT INTO products(name, description, price) VALUES ('{name}','{descr}',{price})"
        cursor.execute(query)

    if choice == 3:
        break



connection.close()
