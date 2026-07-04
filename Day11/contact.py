print("====== CONTACT BOOK ======")

contacts = {
     "Rahul": "9876543210",
    "Priya": "9988776655",
    "Amit": "9123456789"
}

def main_menu():
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print(f"Contact {name} added successfully!")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found!")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name in contacts:
        new_number = input("Enter new contact number: ")
        contacts[name] = new_number
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        contacts.pop(name)
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def exit_program():
    print("Exiting...")        

while True:
    main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_contacts(contacts)
    elif choice == 2:
        add_contact(contacts)
    elif choice == 3:
        search_contact(contacts)
    elif choice == 4:
        update_contact(contacts)
    elif choice == 5:
        delete_contact(contacts)
    elif choice == 6:
        exit_program()
        break
    else:
        print("Invalid choice!")