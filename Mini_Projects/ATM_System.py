print("Welcome to the ATM System")

Balance=[1000]

def menu():
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f"Your current balance is: ${sum(Balance)}")    #vs code recommmed me to use sum() function to get the total balance 

def deposit_money():
    amount = float(input("Enter the amount to deposit: "))
    Balance.append(amount)
    print(f"Amount ${amount} deposited successfully.")
    print(f"Your current balance is: ${sum(Balance)}")

def withdraw_money():
    amount = float(input("Enter the amount to withdraw: "))
    if amount > sum(Balance):
        print("Insufficient balance.")
    else:
        Balance.append(-amount)
        print(f"Amount ${amount} withdrawn successfully.")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit_money()
    elif choice == 3:
        withdraw_money()
    elif choice == 4:
        print("Thank you for using the ATM System.")
        break
    else:
        print("Invalid choice. Please try again.")
