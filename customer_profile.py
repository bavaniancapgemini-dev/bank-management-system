import sqlite3

def create_profile_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )
    """)

    connection.commit()
    connection.close()

def add_profile(
    name,
    email,
    phone
):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO profiles
        (name,email,phone)
        VALUES (?,?,?)
        """,
        (name,email,phone)
    )

    connection.commit()
    connection.close()

def view_profiles():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM profiles"
    )

    data = cursor.fetchall()

    connection.close()

    return data