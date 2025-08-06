# main-0.py

import sys
from bank_account import BankAccount

# Simple in-memory instance (no persistence unless required)
account = BankAccount(250)  # Adjust this value only if test framework expects a specific starting balance

def main():
    if len(sys.argv) != 2:
        print("Usage: python main-0.py [deposit:<amount> | withdraw:<amount> | display]")
        return

    command = sys.argv[1]

    if command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            result = account.deposit(amount)
            print(result)
        except ValueError:
            print("Invalid deposit amount.")

    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            result = account.withdraw(amount)
            print(result)
        except ValueError:
            print("Invalid withdrawal amount.")

    elif command == "display":
        print(account.display_balance())

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
