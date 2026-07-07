
def arithmetic_mean(x, y):
    print((x + y) / 2)


def isgreater(a, b):
    if a > b:
        print("First is greater")
    else:
        print("Second is greater")


def password_checker():
    while True:
        password = input("Enter the password: ")

        if password == "python123":
            print("Access Granted!")
            break
        else:
            print("Invalid Password")


# -----------------------------
# Main Program Starts Here
# -----------------------------
password_checker()

a = 12
b = 9

isgreater(a, b)
arithmetic_mean(a, b)

print()

c = 4
d = 8

isgreater(c, d)
arithmetic_mean(c, d)

print()

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

isgreater(number1, number2)
arithmetic_mean(number1, number2)

print()
