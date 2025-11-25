print("Welcome To The Student Data Organizer!")

print()

students=[]   #List to store all student records

all_subjects= set()

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    print()
    x=int(input("enter your choice: "))



# 1. Add Student
    if x == 1:
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        date_of_birth = input("Enter date of birth (dd-mm-yyyy): ")
        subjects = set(input("Enter subjects (comma separated): ").split(","))
      

        student = {    #Dictonary for student details
            
            "Date of birth": (student_id, date_of_birth),  # tuple
            "student_id" : student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
            
        }

        students.append(student)

        all_subjects.update(subjects)
        
        print()
        print(f"\nStudent {name} added successfully!")

        print("-"*20)
             


# 2. Display All Students

    elif x==2:
        print("----Display All Students----")

        if not students:
            print("NO Student Record Available. ")

        else:
            print("\nAll students:")
            for i in students:
                print(f"ID: {i['student_id']}| Name: {i['name']}| Age: {i['age']}| "
                      f"Grade: {i['grade']}| Subjects: {', '.join(i['subjects'])}")
                
                print("-"*20)


# 3 Update Student Information

    elif x==3:
        stu_id=input("enter student ID update: ")
      
        for i in students:
            if i['Date of birth'][0] == stu_id:
               
                print("What do you want to update?")
                print("1. Age")
                print("2. Subjects")
                y = input("Enter choice: ")
                if y == "1":
                    new_age = int(input("Enter new age: "))
                    student["Age"] = new_age
                    print("Age updated successfully!")
                elif y == "2":
                    new_subjects = set(input("Enter new subjects (comma separated): ").split(","))
                    student["Subjects"] = new_subjects

                    subjects.update(new_subjects)
                    print("Subjects updated successfully!")
                else:
                    print("Invalid update option.")
                break

            else:
                print("Student not found.")

            print("-"*20)


# 4. Delete Student


    elif x == 4:
        stu_id = input("Enter Student ID to delete: ")
     
        for i in range(len(students)):
            if students[i]['Date of birth'][0] == stu_id:
                del students[i]   # delete using del
                found = True
                print("Student deleted successfully!")
                
            else:
                print("Student not found.")
            print("-"*20)

# 5. Display Subjects Offered

    elif x == 5:

        print("\nUnique Subjects Offered:")
        for subject in sorted(all_subjects):
            print(subject)

        print("-"*20)

# 6. Exit

        print()
    elif x == 6:
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")
        
        print("-"*20)

    
    






        
        







