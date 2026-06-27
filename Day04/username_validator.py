name=input("enter your name: ")
while len(name) < 5 or name.find(" ") != -1 or not name[0].isalpha():
    name=input("enter your name: ")
age=int(input("Enter your age: "))
while age < 18:
    print("You must be at least 18 years old.")
    age=int(input("Enter your age: "))
print(f"Registration successful.Welcome, {name}!")