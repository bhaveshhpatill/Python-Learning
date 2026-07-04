print("====== Attendance System ======")




attendance = {
    "Rahul": "Present",
    "Priya": "Absent",
    "Amit": "Present"
}
def main_menu():
    print("1. View Attendance")
    print("2. Mark Present")
    print("3. Check Student")
    print("4. Remove Student")
    print("5. Total Students Present")
    print("6. Exit")

def view_attendance(attendance):
    if not attendance:
        print("No attendance records found.")
    else:
        print("Attendance Records:")
        for name, status in attendance.items():
            print(f"{name}: {status}")

def mark_present(attendance):
    name = input("Enter student name to mark present: ")
    if name in attendance:
     attendance[name] = "Present"
    else:
        attendance[name] = "Present"
        print("New student added and marked present.")


def check_student(attendance):
    name = input("Enter student name to check: ")
    if name in attendance:
        print(f"{name} is marked as {attendance[name]}.")
    else:
        print("Student not found!")

def remove_student(attendance):
    name = input("Enter student name to remove: ")
    if name in attendance:
        attendance.pop(name)
        print(f"{name} removed from attendance records.")
    else:
        print("Student not found!")

def total_students_present(attendance):
   total_present = sum(1 for status in attendance.values() if status == "Present")
   print(f"Total students present: {total_present}")

def exit_program():
    print("Exiting...")                        

while True:
    main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_attendance(attendance)
    elif choice == 2:
        mark_present(attendance)
    elif choice == 3:
        check_student(attendance)
    elif choice == 4:
        remove_student(attendance)
    elif choice == 5:
        total_students_present(attendance)
    elif choice == 6:
        exit_program()
        break
    else:
        print("Invalid choice! Please try again.")    