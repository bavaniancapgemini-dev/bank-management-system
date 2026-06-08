import sqlite3

def create_branch_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS branches(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        branch_name TEXT,
        city TEXT
    )
    """)

    connection.commit()
    connection.close()

def add_branch(name, city):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO branches
        (branch_name, city)
        VALUES (?,?)
        """,
        (name, city)
    )

    connection.commit()
    connection.close()

def view_branches():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM branches"
    )

    data = cursor.fetchall()

    connection.close()

    return data