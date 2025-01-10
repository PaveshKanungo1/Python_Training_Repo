class Bank:
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        if initial_balance < 0:
            raise ValueError("Initial Balance can't be negative")
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def check_balance(self):
        return self.balance

class SavingsAccount(Bank):
    INTEREST_RATE = 0.03
    TRANSACTION_LIMIT = 5

    def __init__(self, account_holder , initial_balance = 0):
        super().__init__(account_holder, initial_balance)
        self.transactions = 0
        self.rewards_points = 0

    def deposit(self, amount):
        super().deposit(amount)
        self.transactions += 1
        self._update_rewards(amount)
        self._check_transaction_limit()

    def withdraw(self, amount):
        super().withdraw(amount)
        self.transactions += 1
        self._check_transaction_limit()

    def calculate_interest(self):
        return self.balance * self.INTEREST_RATE
    
    def check_loan_eligibility(self):
        return self.balance >= 1000  
    
    def _update_rewards(self, amount):
        self.rewards_points += int(amount // 100)

    def _check_transaction_limit(self):
        if self.transactions > self.TRANSACTION_LIMIT:
            print("Warning: Transaction limit exceeded!")

def main():
    savings = SavingsAccount("Pavesh", 500)
    savings.deposit(200)
    print("Balance:", savings.check_balance())
    print("Interest Earned:", savings.calculate_interest())
    print("Loan Eligible:", savings.check_loan_eligibility())
    savings.deposit(300)
    print("Rewards Points:", savings.rewards_points)

if __name__ == "__main__":
    main()

    

