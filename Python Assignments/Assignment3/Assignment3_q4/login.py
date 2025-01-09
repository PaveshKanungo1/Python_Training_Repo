
from user_auth.registration import users

def login_user(username, password):
    if username in users and users[username] == password:
        return True, "Login successful."
    return False, "Invalid username or password."
