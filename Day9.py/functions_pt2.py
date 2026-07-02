# =====================================
# Functions Practice - Part 2
# Day 9
# =====================================

# -------------------------------------
# 1. Simple Function
# -------------------------------------

def say_hello():
    print("Hello")

say_hello()


# -------------------------------------
# 2. Function with Return
# -------------------------------------

def square_number(num):
    return num * num

print(square_number(5))


# -------------------------------------
# 3. Function with Parameter
# -------------------------------------

def welcome_user(name):
    print(f"Welcome, {name}!")

name = input("Enter your name: ")
welcome_user(name)


# -------------------------------------
# 4. Addition Function
# -------------------------------------

def add(a, b):
    return a + b

x = add(2, 3)
print(x)


# -------------------------------------
# 5. Multiplication Function
# -------------------------------------

def multiply(a, b):
    return a * b

answer = multiply(5, 8)
print(f"5 multiplied by 8 is {answer}")

answer = multiply(3, 5)
print(f"3 multiplied by 5 is {answer}")


# -------------------------------------
# 6. Local Variable Example
# -------------------------------------

def test():
    y = 50
    return y

result = test()
print(result)


# -------------------------------------
# 7. Square Function
# -------------------------------------

def square(x):
    answer = x * x
    return answer

num = square(6)
print(num)


# -------------------------------------
# 8. Find Maximum Number
# -------------------------------------

def my_max(numbers):

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


print(my_max([1, 2, 3, 4, 5]))