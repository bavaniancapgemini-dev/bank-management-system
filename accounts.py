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

def search_account(name):

    import sqlite3

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM accounts WHERE name LIKE ?",
        ("%" + name + "%",)
    )

    data = cursor.fetchall()

    connection.close()

    return data

def delete_account(account_id):

    import sqlite3

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM accounts WHERE id = ?",
        (account_id,)
    )

    connection.commit()
    connection.close()

def account_statement(account_id):

    import sqlite3

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM accounts WHERE id=?",
        (account_id,)
    )

    account = cursor.fetchone()

    connection.close()

    return account