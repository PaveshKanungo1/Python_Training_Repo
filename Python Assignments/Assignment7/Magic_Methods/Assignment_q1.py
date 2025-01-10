class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"Transaction(amount={self.amount}, description='{self.description}')"

    def __str__(self):
        return f"Transaction of Rs {self.amount}: {self.description}"

    def __eq__(self, other):
        if isinstance(other, Transaction):
            return self.amount == other.amount and self.description == other.description
        return False

    def __add__(self, other):
        if isinstance(other, Transaction):
            return Transaction(self.amount + other.amount, f"{self.description} & {other.description}")
        return NotImplemented

transaction1 = Transaction(100, "Grocery shopping")
transaction2 = Transaction(200, "Electronics purchase")
transaction3 = Transaction(100, "Grocery shopping")

print(transaction1) 
print(repr(transaction2))  
print(transaction1 == transaction3) 
print(transaction1 + transaction2)  