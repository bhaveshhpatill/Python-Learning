# ===== Notes Manager ======

# 1. View Files
# 2. Open File
# 3. Create File
# 4. Delete File
# 5. Exit


print("===== Notes Manager ======")

notes = []

def menu():
    print("\n1. View Files")
    print("2. Open File")
    print("3. Create File")
    print("4. Delete File")
    print("5. Exit")

def view_files():
    print("\nFiles:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")

def open_file():
    view_files()
    choice = int(input("\nEnter the file number to open: "))
    if 1 <= choice <= len(notes):
        filename = notes[choice - 1]
        with open(filename, "r") as file:
            content = file.read()
            print(f"\nContent of {filename}:\n{content}")
    else:
        print("Invalid choice.")

def create_file():
    filename = input("\nEnter the name of the new file: ")
    with open(filename, "w") as file:
        content = input("Enter content for the file:\n")
        file.write(content)
    notes.append(filename)
    print(f"{filename} created successfully.")

def delete_file():
    view_files()
    choice = int(input("\nEnter the file number to delete: "))
    if 1 <= choice <= len(notes):
        filename = notes.pop(choice - 1)
        import os
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    else:
        print("Invalid choice.")
   
   

while True:
        menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_files()
        elif choice == "2":
            open_file()
        elif choice == "3":
            create_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("Exiting Notes Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


