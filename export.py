import sqlite3
import json

def export_accounts():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM accounts"
    )

    data = cursor.fetchall()

    with open(
        "accounts.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    connection.close()