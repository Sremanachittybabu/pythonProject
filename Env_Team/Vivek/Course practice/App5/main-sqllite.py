import sqlite3

import sqlite3


def create_table():
    # Connect to SQLite database (it will create a new database if not exists)
    conn = sqlite3.connect('lite.db')
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # Example: Create a table in the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store (
            item TEXT,
            quantity INTEGER,
            price,REAL
        )
        ''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store (item,quantity,price) VALUES (?,?,?)",
                   (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    # Fetch all rows from the result set
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=?,price=?  WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()



print(view())
insert('Wine Glass', 5, 1.5)
print(view())
delete('Wine Glass')
print(view())
update(2,5,'Coffee cup')
print(view())
