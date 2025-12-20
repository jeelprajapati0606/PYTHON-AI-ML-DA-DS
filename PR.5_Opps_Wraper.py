#  --------- Person Class ---------
class person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def display(self):
        print("Name:", self.name)
        print("Age: ",self.age)

#  --------- Employee Class ---------

class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        self.__employee_id = employee_id  
        self.__salary = salary

# set method
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id


    def set_salary(self, salary):
        self.__salary = salary

#  get method
    def get_employee_id(self):
        return self.__employee_id
    
    def get_salary(self):
        return self.__salary
    
    def display(self):
        super().display()
        print("employee ID :", self.get_employee_id())
        print("Salary   :", self.get_salary())

    def __del__(self):
        print("Employee Object Destroyed!")


#  --------- Manager Class ---------
class Manager(employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department : ", self.department)

#  --------- Developer Class ---------

class developer(employee):
    def __init__(self, name, age, employee_id, salary, language):
        super().__init__(name, age, employee_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language: ", self.language)

# --------- Menu Driven Program ---------

records = []

print("WELCOME TO EMPLOYEE MANAGEMENT SYSTEM")

while True:
    print("\n1. Add person")
    print("2. Add employee")
    print("3. Add Manager")
    print("4. Add Developer")
    print("5. Show All Records")
    print("6. Exit")

    choice = int(input("\nEnter choice: "))


    if choice == 1:
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))

        p=person(n, a)
        records.append(p)

        print(f"person created with name: {p.name} and age: {p.age}")

        print("\nPerson Added Successfully!")

    elif choice == 2:
        print("Employee Details: ")
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))
        em_id = input("Enter Employee ID: ")
        s = float(input("Enter Salary: "))
        
        e= employee(n, a, em_id, s)

        records.append(e)

        print(f"Employee Created With Name: {e.name}, Age: {e.age}, ID: {e.get_employee_id()} and Salary: ${e.get_salary()}")
        print("\nEmployee Added Successfully!")

    elif choice == 3:
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))
        em_id = input("Enter Employee ID: ")
        s = float(input("Enter Salary: "))
        d = input("Enter Department: ")

        m= Manager(n, a, em_id, s, d)
        records.append(m)

        print(f"Manager Created With Name: {m.name}, Age: {m.age}, ID: {m.get_employee_id()}, Salary: ${m.get_salary()} And Department {m.department}.")

        print("\nManager Added Successfully!")

    elif choice == 4:
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))
        em_id = input("Enter Employee ID: ")
        s = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")

        d = developer(n, a, em_id, s, lang)
        records.append(d)
        
        print(f"Develpoer Created With Name: {d.name}, Age: {d.age}, ID: {d.get_employee_id()}, Salary: ${d.get_salary()}, language: {d.language}.")
        print("\nDeveloper Added Successfully!")

    elif choice == 5:
        if not records:
            print("NO Records found!")
            break 

        else:
            print("\nChoose Details to show:")
            print("1. person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")

            a= int(input("Enter Your Choice: "))

            for obj in records:
                if a == 1 and p:
                    print("\n--- Person Details ---")
                    issubclass(person, employee)
                    p.display()
                    break
                    

                elif a == 2 and e:
                    print("\n--- Employee Details ---")
                    issubclass(employee, person)
                    e.display()
                    break

                elif a == 3 and m:
                    print("\n--- Manager Details ---")
                    issubclass(employee,Manager)
                    m.display()
                    break

                elif a == 4 and d:
                    print("\n--- Developer Details ---")
                    issubclass(employee, Manager)
                    issubclass(employee,person)
                    d.display()
                    break

                else:
                    print("please enter choice 1 to 4.")
                    break
                   
    elif choice == 6:
        print("Existing the system. All resources have been freed. \n\nGoodbye!")
        break

    else:
        print("Invalid choice")
          