import sqlite3

def create_audit_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT
    )
    """)

    connection.commit()
    connection.close()

def log_action(action):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO audit_logs(action)
        VALUES (?)
        """,
        (action,)
    )

    connection.commit()
    connection.close()

def view_logs():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM audit_logs"
    )

    logs = cursor.fetchall()

    connection.close()

    return logs