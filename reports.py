import sqlite3

def total_money():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT SUM(balance) FROM accounts"
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def richest_customer():

    import sqlite3

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM accounts ORDER BY balance DESC LIMIT 1"
    )

    customer = cursor.fetchone()

    connection.close()

    return customer