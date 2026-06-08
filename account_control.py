import sqlite3
def create_status_column():

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            ALTER TABLE accounts
            ADD COLUMN status TEXT
            """
        )

    except:

        pass

    connection.commit()

    connection.close()

def freeze_account(account_id):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE accounts
        SET status='Frozen'
        WHERE id=?
        """,
        (account_id,)
    )

    connection.commit()

    connection.close()

def unfreeze_account(account_id):

    connection = sqlite3.connect("bank.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE accounts
        SET status='Active'
        WHERE id=?
        """,
        (account_id,)
    )

    connection.commit()

    connection.close()