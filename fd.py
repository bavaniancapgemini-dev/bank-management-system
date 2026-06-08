import sqlite3

def create_fd_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fixed_deposits(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        amount REAL,
        years INTEGER
    )
    """)

    connection.commit()

    connection.close()

def create_fd(name, amount, years):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO fixed_deposits
        (customer_name, amount, years)
        VALUES (?, ?, ?)
        """,
        (name, amount, years)
    )

    connection.commit()

    connection.close()

def view_fd():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM fixed_deposits"
    )

    data = cursor.fetchall()

    connection.close()

    return data