from models.account import Account
from utils.helper import get_valid_amount, print_line

account = Account()

def display_balance():
    print_line()
    print("Balance:", account.balance)
    print_line()

def deposit_money():
    amount = get_valid_amount("Enter amount: ")
    account.balance += amount
    account.add_transaction(f"Deposited {amount}")
    print("Deposit done!")

def withdraw_money():
    amount = get_valid_amount("Enter amount: ")

    if amount > account.balance:
        print("Insufficient balance")
    else:
        account.balance -= amount
        account.add_transaction(f"Withdrew {amount}")
        print("Withdrawal done!")

def show_statement():
    print_line()
    for t in account.transactions:
        print(t)
    print_line()