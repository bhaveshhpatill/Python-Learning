print("nnotes manager v2")


import os
notes=[os.listdir(".")]

def menu():     
    print("\n1. View Files")
    print("2. Open File")
    print("3. Create File")
    print("4. Exit")    

def view_files():
    notes = os.listdir(".")
    print("\nFiles:")
    txt_files = []

    for note in notes:
        if note.endswith(".txt"):
            txt_files.append(note)

    for i, note in enumerate(txt_files, start=1):
        print(f"{i}. {note}")

    return txt_files

def open_file():
    notes = view_files()
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

    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "w") as file:
        content = input("Enter content for the file:\n")
        file.write(content)        

def exit_program():
    print("Exiting the program.")
    exit()  \

while True:
    menu()
    try:
        choice = int(input("\nEnter your choice: "))
    except:
        print("Please enter a valid number.")
        continue
    
    if choice == "1":
        view_files()
    elif choice == "2":
         open_file()
    elif choice == "3":
        create_file()
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice. Please try again.")

