from user_auth.registration import register_user
from user_auth.login import login_user

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            success, message = register_user(username, password)
            print(message)

        elif choice == '2':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            success, message = login_user(username, password)
            print(message)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()