def check_role(username):

    if username == "admin":

        return "Admin"

    elif username.startswith("emp"):

        return "Employee"

    else:

        return "Customer"