
def check_prime(user_input):
    prime = True
    for i in range(2, user_input):
        if user_input%i == 0:
            prime = False
            break
    return prime

def main():
    print("Program to check prime, composite or neither(for negative or zero values)")
    try:
        user_input = int(input("Enter your input:"))

        if user_input <= 0:
            print(user_input, " is neither prime nor composite")
        else:
            prime = check_prime(user_input)
            if prime == True:
                print(user_input, " is a prime number")
            else:
                print(user_input, " is a composite number")

    except ValueError:
        print("Invalid Input. Please enter a valid number")
        

if __name__ == "__main__":
    main() 