# =============================
# Mini Project - Simple To-Do List
# =============================

tasks = []

tasks.append(input("\nEnter Task 1: "))
tasks.append(input("Enter Task 2: "))
tasks.append(input("Enter Task 3: "))

print("\nYour Tasks:")

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")

completed = int(input("\nEnter completed task number: "))

tasks.pop(completed - 1)

print("\nTask completed successfully!")

print("\nRemaining Tasks:")

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")