print("====== Welcome to SHOPPING CART=====")

cart=[]

while True:
    print("\n Main Meanu:")
    print("1. view the cart")
    print("2. add item to the cart")
    print("3. remove item from the cart")
    print("4. exit")
    choice = int(input("\nEnter your choice: "))

    if choice < 0 or choice > 4:
        print("Invalid choice, please try again.")
    elif choice == 1 :
          if not cart:
             print("Your cart is empty.")
          else:
            for i, item in enumerate(cart, start=1):
                  print(f"{i}. {item}")
    elif choice == 2 :
        item = input("\nEnter the item to add: ")
        cart.append(item)
        print(f"{item} added to the cart.")
    elif choice == 3:
        item = input("Enter the item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from the cart.")
        else:
            print("Item not found in the cart.")
    elif choice == 4:
        print("\nThank you for using SHOPPING CART!")
        break
    else:
        print("Invalid choice, please try again.")