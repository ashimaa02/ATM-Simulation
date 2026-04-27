def get_valid_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount <= 0:
                print("Invalid amount!")
            else:
                return amount
        except:
            print("Enter numbers only!")

def print_line():
    print("=" * 30)