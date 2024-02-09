import psycopg2


def create_table():
    # Connect to SQLite database (it will create a new database if not exists)
    conn = psycopg2.connect("dbname='database1' user='postgres' password='am107ec068' host='localhost' port='5432'")
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # Example: Create a table in the database
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='am107ec068' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store (item,quantity,price) VALUES (%s,%s,%s) ",
                   (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='am107ec068' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    # Fetch all rows from the result set
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='am107ec068' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='am107ec068' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=%s,price=%s  WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
print(view())
insert('Orange', 5, 1.5)
print(view())
delete('Orange')
print(view())
insert('Orange', 5, 1.5)
update(2,5,'Orange')
print(view())
