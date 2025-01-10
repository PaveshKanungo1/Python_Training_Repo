class Bank:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        if initial_balance < 0:
            raise ValueError("Initial Balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited Rs {amount:.2f}. New balance is Rs {self.balance:.2f}.")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew Rs {amount:.2f}. New balance is Rs {self.balance:.2f}.")

    def check_balance(self):
        print(f"The current balance is Rs {self.balance:.2f}.")
        return self.balance
    
def main():
    try:
        account = Bank("Pavesh, 100")
        account.deposit(100)
        account.withdraw(50)
        account.check_balance()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
