import sqlite3

def create_customer_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    connection.commit()
    connection.close()

def register_customer(username, password):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO customers(username,password) VALUES (?,?)",
        (username, password)
    )

    connection.commit()
    connection.close()

def customer_login(username, password):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM customers
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    connection.close()

    return user