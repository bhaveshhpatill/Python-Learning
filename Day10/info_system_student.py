print("====== Student Information System ======")


student = {
    "Name": "Bhavesh",    
    "Age": 21,
    "College": "RAIT",
    "City": "Mumbai",
    "CGPA": 7.5,
    "Skills": ["Python", "Java", "C++"]
    }
def mean():
    print("1. View Student Details")
    print("2. Update CGPA")
    print("3. Add Skill")
    print("4. Remove Skill")
    print("5. Exit")
    
def view_student_details():
    print("Student Details:")
    for key, value in student.items():
        print(f"{key}: {value}")

def CGPA():
    new_cgpa = float(input("Enter new CGPA: "))
    student["CGPA"] = new_cgpa
    print("CGPA updated successfully!")

def add_skill():
    new_skill = input("Enter new skill to add: ")
    student["Skills"].append(new_skill)
    print("Skill added successfully!")

def remove_skill():
    skill_to_remove = input("Enter skill to remove: ")
    if skill_to_remove in student["Skills"]:
        student["Skills"].remove(skill_to_remove)
        print("Skill removed successfully!")
    else:
        print("Skill not found!")  

def exit():
    print("Exiting...")
             

while True:
    mean()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_student_details()
    elif choice == 2:
        CGPA()
    elif choice == 3:
        add_skill()
    elif choice == 4:
        remove_skill()
    elif choice == 5:
        exit()
        break
    else:
        print("Invalid choice!")
                 
