import sqlite3

def total_bank_balance():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT SUM(balance) FROM accounts"
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def analytics_report():

    print()

    print("BANK ANALYTICS")

    print(
        "Total Money:",
        total_bank_balance()
    )