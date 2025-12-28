# app.py

from lab import BankAccount

def main():
    account = BankAccount("1234567890", 1000)

    print("Account Number:", account.get_account_number())
    print("Initial Balance:", account.get_balance())

    account.deposit(500)
    print("After Deposit:", account.get_balance())

    account.withdraw(200)
    print("After Withdrawal:", account.get_balance())

if __name__ == "__main__":
    main()
