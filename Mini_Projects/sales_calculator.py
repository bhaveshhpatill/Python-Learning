
products = {
    "milk": 35,
    "bread": 40,
    "butter": 60,
    "rice": 70,
    "sugar": 50,
}

def menu():
   print("""========= Reliance Retail =========

1. Milk        ₹35
2. Bread       ₹40
3. Butter      ₹60
4. Rice        ₹70
5. Sugar       ₹50

""") 

while True:
    menu()

    product = input("Enter Product: ").lower()

    if product not in products:
        print("Invalid product name. Please try again.")
        continue

    quantity = int(input("Enter Quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    subtotal = quantity * products[product]

    break
print(f"Subtotal: ₹{subtotal}")

if subtotal > 10000:
    discount = subtotal * 15 / 100
    subtotal = subtotal - discount

print(f"Final Bill: ₹{subtotal}")



