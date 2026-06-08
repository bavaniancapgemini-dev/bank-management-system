import sqlite3

def create_account(name, balance):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO accounts(name, balance) VALUES (?, ?)",
        (name, balance)
    )

    connection.commit()
    connection.close()

def view_accounts():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM accounts")

    data = cursor.fetchall()

    connection.close()

    return data