class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, msg):
        self.transactions.append(msg)