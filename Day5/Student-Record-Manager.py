print("====Student Records Manager===")

students = []

student1 = input("Enter Student 1 Name: ")
student2 = input("Enter Student 2 Name: ")
student3 = input("Enter Student 3 Name: ")

students = [student1, student2, student3]
print(students)

student_name = input("Enter Student Name to Remove: ")

if student_name in students:
     students.remove(student_name)
     print("Student removed successfully!")
else:
    print("Student not found!")

print("Updated Student Records:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")







