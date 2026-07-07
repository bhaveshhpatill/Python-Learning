print("======Calculator=====")


while True:
    print("1. Addition")
    print("2. Subtraction")          
    print("3. multiplaction")
    print("4. Divison")
    print("5. Exit")
    
    choice = int (input("Enter your choice (1-5): "))

    if 1<= choice > 5 :
        print("Invalidd choice.pleas try again")

    elif choice == 1:
      num1=int(input("Enter the number 1: "))
      num2=int(input("Enter thwe numer2: "))
      print(num1+num2)
    
    elif choice == 2:
       num1=int(input("Enter the number 1: "))
       num2=int(input("Enter thwe numer2: "))
       print(num1-num2)
    
    elif choice == 3:
       num1=int(input("Enter the number 1: "))
       num2=int(input("Enter thwe numer2: "))
       print(num1*num2)
     
    elif choice ==4:
        num1=int(input("Enter the number 1: "))
        num2=int(input("Enter thwe numer2: "))
        print(num1/num2)

    elif choice == 5 :
       print("exiting thank you for using my calulator ")
       break    