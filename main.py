from database import create_table
from accounts import create_account, view_accounts
from transactions import deposit, withdraw
from reports import total_money
from utils import title

create_table()

while True:

    title()

    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Total Bank Money")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Customer Name: ")

        balance = float(
            input("Opening Balance: ")
        )

        create_account(name, balance)

        print("Account Created")

    elif choice == "2":

        accounts = view_accounts()

        for account in accounts:

            print(account)

    elif choice == "3":

        account_id = int(
            input("Account ID: ")
        )

        amount = float(
            input("Deposit Amount: ")
        )

        deposit(account_id, amount)

        print("Money Deposited")

    elif choice == "4":

        account_id = int(
            input("Account ID: ")
        )

        amount = float(
            input("Withdraw Amount: ")
        )

        withdraw(account_id, amount)

        print("Money Withdrawn")

    elif choice == "5":

        print(
            "Total Money:",
            total_money()
        )

    elif choice == "6":

        break

    else:

        print("Invalid Choice")