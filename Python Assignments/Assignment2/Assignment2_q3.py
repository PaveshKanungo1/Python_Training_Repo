class ATM:
    def __init__(self, init_balance = 0):
        self.balance = init_balance
    
    def check_balance(self):
        print(f"Your Bank's Balance is Rs {self.balance}")

    def deposit(self, amt):
        if amt <= 0:
            print("Invalid deposit amount. Please enter a positive number.")
        else:
            self.balance += amt
            print(f"Rs {amt:.2f} is deposited successfully in your account")

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid deposit amount. Please enter a positive number.")
        elif amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print(f"Rs {amt:.2f} withdrawn successfully")
    
def main():
    atm = ATM()
    while True:
        print("Choose Operations: ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        try:
            choice = int(input("Please select an option(1-4):"))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter deposit amount: "))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using my ATM")
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input. Please Enter a number.")

if __name__ == "__main__":
    main()



