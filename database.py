import sqlite3

def create_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        balance REAL
    )
    """)

    connection.commit()
    connection.close()