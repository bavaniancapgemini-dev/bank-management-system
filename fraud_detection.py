def check_fraud(amount):

    if amount > 100000:

        return True

    return False

    if check_fraud(amount):

        print("WARNING")
        print("Large Transaction Detected")