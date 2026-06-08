import sqlite3

def create_employee_table():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        salary REAL
    )
    """)

    connection.commit()
    connection.close()

def add_employee(name, role, salary):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (name, role, salary)
        VALUES (?, ?, ?)
        """,
        (name, role, salary)
    )

    connection.commit()
    connection.close()

def view_employees():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    connection.close()

    return data