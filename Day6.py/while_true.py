
# ======================================
# Day 6 - While Loops Practice
# ======================================


# -----------------------------
# 1. Password Checker
# -----------------------------

# password = "python123"

# while True:
#     password = input("Enter the password: ")

#     if password == "python123":
#         print("Access Granted!")
#         break

#     print("Invalid Password")


# -----------------------------
# 2. Name Validation
# -----------------------------

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name.")
#     name = input("Enter your name: ")

# print(f"Hello {name}")


# -----------------------------
# 3. Age Validation
# -----------------------------

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Your age is not valid.")
#     age = int(input("Enter your age: "))

# print(f"Your age is {age}")


# -----------------------------
# 4. Number Guessing Game
# -----------------------------

import random

secret = random.randint(1, 10)

print("Guess the number between 1 and 10")

guess = int(input("Guess: "))

while guess != secret:
    print("Incorrect!")
    guess = int(input("Guess: "))
    
print("You won!!")
