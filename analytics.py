import sqlite3

def total_accounts():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM accounts"
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def total_loans():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM loans"
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def dashboard():

    print()
    print("----- ANALYTICS -----")

    print(
        "Total Accounts:",
        total_accounts()
    )

    print(
        "Total Loans:",
        total_loans()
    )