import sqlite3

def apply_monthly_interest():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE accounts
        SET balance = balance * 1.01
        """
    )

    connection.commit()
    connection.close()