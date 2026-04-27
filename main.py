from services import atm_operations

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        atm_operations.display_balance()
    elif choice == '2':
        atm_operations.deposit_money()
    elif choice == '3':
        atm_operations.withdraw_money()
    elif choice == '4':
        atm_operations.show_statement()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice")