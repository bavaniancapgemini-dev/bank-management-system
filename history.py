import sqlite3


def create_history_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT
    )
    """)

    connection.commit()
    connection.close()

def save_history(action):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO history(action) VALUES(?)",
        (action,)
    )

    connection.commit()
    connection.close()

def view_history():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM history")

    data = cursor.fetchall()

    connection.close()

    return data