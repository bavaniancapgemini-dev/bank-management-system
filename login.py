def login():

    username = input("Username: ")

    password = input("Password: ")

    if username == "admin" and password == "1234":

        return True

    return False