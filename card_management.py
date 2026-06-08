import sqlite3
def create_card_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cards(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        card_number TEXT
    )
    """)

    connection.commit()

    connection.close()

import random

def issue_card(name):

    card = str(
        random.randint(
            1000000000000000,
            9999999999999999
        )
    )

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO cards
        (customer_name, card_number)
        VALUES (?,?)
        """,
        (name, card)
    )

    connection.commit()

    connection.close()

    return card