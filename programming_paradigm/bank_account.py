class BankAccount:
    def __init__(self, account_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = float(account_balance)

    def deposit(self, amount):
        """Add money to the account and print confirmation."""
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist; else print error."""
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
