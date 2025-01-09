
users = {}

def register_user(username, password):
    if username in users:
        return False, "Username already exists."
    users[username] = password
    return True, "User registered successfully."
