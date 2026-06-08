import sqlite3

def deposit(account_id, amount):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, account_id)
    )

    connection.commit()
    connection.close()

def withdraw(account_id, amount):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, account_id)
    )

    connection.commit()
    connection.close()

def transfer_money(sender, receiver, amount):

    import sqlite3

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, sender)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, receiver)
    )

    connection.commit()
    connection.close()