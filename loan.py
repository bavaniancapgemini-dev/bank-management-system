import sqlite3

def create_loan_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loans(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        amount REAL
    )
    """)

    connection.commit()
    connection.close()

def issue_loan(name, amount):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO loans(customer_name, amount) VALUES (?, ?)",
        (name, amount)
    )

    connection.commit()
    connection.close()

def view_loans():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM loans")

    data = cursor.fetchall()

    connection.close()

    return data