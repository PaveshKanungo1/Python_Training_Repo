class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            if len(new_password) < 6:
                print("New password must be at least 6 characters long.")
                return False
            self.__password = new_password
            print("Password updated successfully.")
            return True
        else:
            print("Old password is incorrect.")
            return False
        
    def verify_password(self, password):
        return self.__password == password

    def display_username(self):
        print(f"Username: {self.username}")

user = UserAccount("Pavesh", "Mypassword123")
user.display_username()

if user.verify_password("securepassword"):
    print("Password verification successful.")
else:
    print("Password verification failed.")

user.set_password("securepassword", "newpass")  
user.set_password("securepassword", "newsecurepassword")

