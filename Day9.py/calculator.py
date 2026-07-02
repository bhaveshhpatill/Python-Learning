print("======Calculator=====")

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b    
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def valueofnum():
    num1=int(input("Enter the number 1: "))
    num2=int(input("Enter thwe numer2: "))
    return num1,num2
def show_menu():
    print("1. Addition")
    print("2. Subtraction")          
    print("3. multiplaction")
    print("4. Divison")
    print("5. Exit")
    return "Please select an option (1-5): "

while True:
    print(show_menu())

    choice = int (input())

    if choice < 1 or choice > 5:
        print("Invalid choice. Please try again.")

    elif choice == 1:
     num1,num2=valueofnum()
     print(add(num1,num2))
    
    elif choice == 2:
       num1,num2=valueofnum()
       print(subtract(num1,num2))
    
    elif choice == 3:
       num1,num2=valueofnum()
       print(multiply(num1,num2))
     
    elif choice ==4:
        num1,num2=valueofnum()
        print(divide(num1,num2))

    elif choice == 5 :
       print("exiting thank you for using my calulator ")
       break    
