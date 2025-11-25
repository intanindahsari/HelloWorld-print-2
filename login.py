from data import data_user

def login(username, password):
    for user in data_user:
        if user[0] == username and user[1] == password:
            return user[2]
    return ""