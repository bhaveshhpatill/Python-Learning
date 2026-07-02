print("=====Student Records Manager=====")


Student= []
while True :
    print("\n1. View Student")
    print("2. Add Student")          
    print("3. Remove Student")
    print("4. Exit")
    choice = int (input("Enter your choice (1-4): "))

    if choice > 4 :
       print("Invalidd choice.pleas try again")
    
    elif choice == '1':
        if not Student:
                  print("No students found.")
        else:
                  print("Student Records:")
        for i, student in enumerate(Student, start=1):
            print(f"{i}. {student}")    

    elif choice=='2':
             Student_name = input("enter the student name to add: ")            
             Student.append(Student_name)
             print(f"Student added: {Student_name}")
            
    
    elif choice =='3':
             Student_number = input("Enter the number of student you want to remove: ")
             Student.pop(int(Student_number)-1)
             print(f"removed succesfully")
 
    elif choice == '4':
             print("exiting")
             break