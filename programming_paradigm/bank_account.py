# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = float(account_balance)

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        if amount > self.account_balance:
            return "Insufficient funds."
        else:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.1f}"

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
