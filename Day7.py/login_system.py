print("======LOGIN SYSTEM====")

valid_username = "admin"
valid_password = "python123"
attempt = 0

while True:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == valid_username and password == valid_password:
        print("login successfully welcome admin")
        break
    else:
        attempt+=1
        if attempt == 5:
         print("to many attempt tried")
         break
        else:
         print(attempt)
         print("Invalid credential")



