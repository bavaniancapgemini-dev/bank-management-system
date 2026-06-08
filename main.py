from database import create_table
from accounts import create_account, view_accounts, search_account, delete_account
from accounts import *
from transactions import deposit, withdraw, transfer_money
from reports import total_money, richest_customer
from utils import title
from history import create_history_table, save_history, view_history
from loan import *
from interest import simple_interest

create_table()
create_history_table()
create_loan_table()

while True:

    title()

    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Total Bank Money")
    print("6. Search Account")
    print("7. Delete Account")
    print("8. Transfer Money")
    print("9. Richest Customer")
    print("10. View History")
    print("11. Issue Loan")
    print("12. View Loans")
    print("13. Interest Calculator")
    print("14. Account Statement")
    print("15. Exit")

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

        save_history(
            f"Deposit: Account {account_id} Amount {amount}"
)

        print("Money Deposited")

    elif choice == "4":

        account_id = int(
            input("Account ID: ")
        )

        amount = float(
            input("Withdraw Amount: ")
        )

        withdraw(account_id, amount)

        save_history(
            f"Withdraw: Account {account_id} Amount {amount}"
)

        print("Money Withdrawn")

    elif choice == "5":

        print(
            "Total Money:",
            total_money()
        )

    elif choice == "6":

        name = input("Enter customer name to search: ")

        results = search_account(name)

        for account in results:

            print(account)

    elif choice == "7":

        account_id = int(
            input("Enter Account ID to delete: ")
        )

        delete_account(account_id)

        print("Account Deleted")

    elif choice == "8":

        sender = int(
            input("Enter Sender's Account ID: ")
        )

        receiver = int(
            input("Enter Receiver's Account ID: ")
        )

        amount = float(
            input("Enter Transfer Amount: ")
        )

        transfer_money(sender, receiver, amount)

        save_history(
            f"Transfer: Account {sender} to Account {receiver} Amount {amount}"
        )

        print("Money Transferred")

    elif choice == "9":

        print(richest_customer())

    elif choice == "10":

        history = view_history()

        for entry in history:

            print(entry)

    elif choice == "11":
        name = input("Customer Name: ")

        amount = float(
            input("Loan Amount: ")
        )

        issue_loan(name, amount)

        save_history(
        f"Loan Issued: {name} {amount}"
    )

        print("Loan Issued")

    elif choice == "12":

        loans = view_loans()

        for loan in loans:

            print(loan)

    elif choice == "13":

        principal = float(input("Principal Amount: "))
        rate = float(input("Interest Rate: "))
        years = float(input("Number of Years: "))

        interest = simple_interest(principal, rate, years)

        print(f"Simple Interest: {interest}")

    elif choice == "14":

        account_id = int(input("Enter Account ID: "))
        account = account_statement(account_id)
        print(account)

    elif choice == "15":

        break

    else:

        print("Invalid Choice")