with open("notes.txt", "a") as file:
    file.write("\nSQL")
with open("notes.txt") as file:
    text = file.read()
    print(text)