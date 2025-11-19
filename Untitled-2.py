def passwordlogintest():
    a= "Email must contain '@' symbol."
    b = "Email must be a string."
    c= "Password must be at least 8 characters long."
    d= "Password must include at least one number."
    e= "Password must include at least one uppercase letter."
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if not isinstance(email, str) or "@" not in email:
        print (a)
    if not isinstance(password, str):
        print (b)
    if len(password) < 8:
        print (c)
    if not any(char.isdigit() for char in password):
        print (d)
    if not any(char.isupper() for char in password):
        print (e)
    else:
        print("email: ", email, "and", "password:", password, "are valid!")
passwordlogintest()