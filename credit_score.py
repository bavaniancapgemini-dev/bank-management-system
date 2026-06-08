import sqlite3

def create_credit_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS credit_scores(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        score INTEGER
    )
    """)

    connection.commit()
    connection.close()

def assign_credit_score(name, score):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO credit_scores
        (customer_name, score)
        VALUES (?,?)
        """,
        (name, score)
    )

    connection.commit()
    connection.close()

def view_credit_scores():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM credit_scores"
    )

    data = cursor.fetchall()

    connection.close()

    return data