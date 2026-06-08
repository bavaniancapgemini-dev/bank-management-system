from login import login
from database import create_table
from accounts import create_account, view_accounts, search_account, delete_account
from accounts import *
from pdf_report import create_pdf_report
from transactions import deposit, withdraw, transfer_money
from reports import total_money, richest_customer
from utils import title
from history import create_history_table, save_history, view_history
from loan import *
from interest import simple_interest
from emi import calculate_emi
from fd import *
from analytics import dashboard
from card_management import *
from account_control import *
from notifications import *
from export import export_accounts
from credit_score import *
from fraud_detection import *
from otp import *
from customer_profile import *
from monthly_interest import *
from employee import *
from audit import *
from password_reset import *
from branch import *
from analytics_v2 import *


create_table()
create_history_table()
create_loan_table()
create_fd_table()
create_card_table()
create_status_column()
create_credit_table()
create_profile_table()
create_employee_table()
create_audit_table()
create_branch_table()
if not login():
    print("Login failed.")
    exit()

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
    print("15. Created Fixed Deposit")
    print("16. View Fixed Deposits")
    print("17. EMI Calculator")
    print("18. Export Accounts")
    print("19. Analytics Dashboard")
    print("20. Generate PDF Report")
    print("21. Issue ATM Card")
    print("22. Freeze Account")
    print("23. Unfreeze Account")
    print("24. Update Customer Profile")
    print("25. Add Customer Profile")
    print("26. View Profiles")
    print("27. Assign Credit Scores")
    print("28. View Credit Scores")
    print("29. Apply Monthly Interest")
    print("30. Employee Management")
    print("31. Add Employee")
    print("32. View Employees")
    print("33. Add Branch")
    print("34. View Branches")
    print("35. View Audit Logs")
    print("36. Reset Password")
    print("37. Advanced Analytics")
    print("38. Exit")

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

        name = input("Customer Name: ")
        amount = float(input("Deposit Amount: "))
        years = int(input("Number of Years: "))

        create_fd(name, amount, years)

        print("Fixed Deposit Created")

    elif choice == "16":

        fds = view_fd()

        for fd in fds:

            print(fd)

    elif choice == "17":

        loan = float(input("Loan Amount: "))
        months = int(input("Number of Months: "))

        emi = calculate_emi(loan, months)

        print(f"EMI: {emi}")

    elif choice == "18":

        export_accounts()

        print("Accounts Exported")

    elif choice == "19":

        dashboard()

    elif choice == "20":

        create_pdf_report()

        print("PDF Report Generated")

    elif choice == "21":
        account_id = int(input("Enter Account ID: "))
        issue_card(account_id)
        print("ATM Card Issued")
    elif choice == "22":

        account_id = int(input("Enter Account ID: "))
        freeze_account(account_id)
        print("Account Frozen")
    elif choice == "23":

        account_id = int(input("Enter Account ID: "))
        unfreeze_account(account_id)
        print("Account Unfrozen")
    
    elif choice == "24":
        name = input("Enter Customer Name: ")
        email = input("Enter Customer Email: ")
        phone = input("Enter Customer Phone: ")
        add_profile(name, email, phone)
        print("Customer Profile Added")
    
    elif choice == "25":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        add_profile(name, email, phone)

        print("Profile Added")

    elif choice == "26":
        for profile in view_profiles():

            print(profile)

    elif choice == "27":
        name = input("Customer Name: ")

        score = int(
            input("Credit Score: ")
        )
        
        assign_credit_score(
            name, score
        )
    
    elif choice == "28":
        for score in view_credit_scores():

            print(score)

    elif choice == "29":
        apply_monthly_interest()
        print("Monthly Interest Applied")

    elif choice == "30":
        print("Employee Management")

    elif choice == "31":
        name = input("Employee Name: ")
        role = input("Role: ")
        salary = float(input("Salary: "))

        log_action(
            f"Employee Added {name}"
        )

    elif choice == "32":
        for employee in view_employees():
            print(employee)

    elif choice == "33":

        name = input("Branch Name: ")
        location = input("Branch Location: ")

        add_branch(name, location)

    elif choice == "34":
        for branch in view_branches():

            print(branch)

    elif choice == "35":
        for log in view_logs():

            print(log)

    elif choice == "36":
        reset_password()

    elif choice == "37":
        analytics_report()

    elif choice == "38":

        break

    else:

        print("Invalid Choice")