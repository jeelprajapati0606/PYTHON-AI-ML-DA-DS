import datetime
import time
import math
import random
import string
import uuid

class MultiUtilityToolkit():

    def datetime_operations(self):
        while True:
            print("\n===== Datetime & Time Operations =====")
            print("1. Display Current Date & Time")
            print("2. Calculate Difference Between Two Dates")
            print("3. Format Current Date")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")
            print("--------------------------------------")

            choice = int(input("Enter your Date-Time option : "))

            if choice == 1:
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\nCurrent Date & Time: {formatted_time}\n")

            elif choice == 2:
                date1 = datetime.datetime.strptime(input("Enter first date (YYYY-MM-DD): "), "%Y-%m-%d")
                date2 = datetime.datetime.strptime(input("Enter second date (YYYY-MM-DD): "), "%Y-%m-%d")
                diff_days = abs((date1 - date2).days)
                print(f"\nDifference: {diff_days} days\n")

            elif choice == 3:
                now = datetime.datetime.now()
                formatted_date = now.strftime("%A, %B %d, %Y")
                print(f"\nFormatted Date: {formatted_date}\n")

            elif choice == 4:
                input("Press Enter to start the stopwatch...")
                start_time = time.time()
                input("Press Enter to stop the stopwatch...")
                end_time = time.time()
                elapsed = round(end_time - start_time, 2)
                print(f"\nElapsed Time: {elapsed} seconds\n")

            elif choice == 5:
                seconds = int(input("Enter countdown seconds: "))
                for i in range(seconds, 0, -1):
                    print(i, end="... ", flush=True)
                    time.sleep(1)
                print("\nTime's up!\n")

            elif choice == 6:
                break

            else:
                print("\nInvalid option! Please try again.\n")

    def math_operations(self):
        while True:
            print("\n===== Mathematical Operations =====")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to Main Menu")
            print("------------------------------------")

            choice = int(input("Enter your Math Option: "))

            if choice == 1:
                num = int(input("Enter a number: "))
                print(f"\nFactorial: {math.factorial(num)}\n")

            elif choice == 2:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                years = float(input("Enter number of years: "))
                amount = principal * (1 + rate / 100) ** years
                print(f"\nCompound Interest Amount: {amount:.2f}\n")

            elif choice == 3:
                degree = float(input("Enter angle in degrees: "))
                radians = math.radians(degree)
                print(f"\nsin({degree}) = {math.sin(radians):.4f}")
                print(f"cos({degree}) = {math.cos(radians):.4f}")
                print(f"tan({degree}) = {math.tan(radians):.4f}\n")

            elif choice == 4:
                print("\nChoose Shape:")
                print("1. Circle")
                print("2. Rectangle")
                shape_choice = int(input("Enter shape choice: "))

                if shape_choice == 1:
                    radius = float(input("Enter radius of circle: "))
                    area = math.pi * radius ** 2
                    print(f"\nArea of Circle: {area:.2f}\n")

                elif shape_choice == 2:
                    length = float(input("Enter length of rectangle: "))
                    width = float(input("Enter width of rectangle: "))
                    area = length * width
                    print(f"\nArea of Rectangle: {area:.2f}\n")

                else:
                    print("\nInvalid shape choice!\n")

            elif choice == 5:
                break

            else:
                print("\nInvalid option! Please try again.\n")

    def random_operations(self):
        while True:
            print("\n===== Random Data Generation =====")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Generate Random Password")
            print("4. Generate Random OTP")
            print("5. Back to Main Menu")
            print("-----------------------------------")

            choice = int(input("Enter your Random Data choice: "))

            if choice == 1:
                rand_num = random.randint(1, 100)
                print(f"\nRandom Number: {rand_num}\n")

            elif choice == 2:
                size = int(input("Enter the number of elements in the list: "))
                rand_list = [random.randint(1, 100) for _ in range(size)]
                print(f"\nRandom List: {rand_list}\n")

            elif choice == 3:
                length = int(input("Enter password length: "))
                characters = string.ascii_letters + string.digits
                password = ''.join(random.choice(characters) for _ in range(length))
                print(f"\nRandom Password: {password}\n")

            elif choice == 4:
                otp = ''.join(random.choice(string.digits) for _ in range(6))
                print(f"\nRandom OTP: {otp}\n")

            elif choice == 5:
                break

            else:
                print("\nInvalid option! Please try again.\n")

    def generate_uuid(self):
        unique_id = uuid.uuid4()
        print("\n===== Generated UUID =====")
        print(f"{unique_id}\n")

    def file_operations(self):
        while True:
            print("\n===== File Operations =====")
            print("1. Create a File")
            print("2. Write to a File")
            print("3. Read from a File")
            print("4. Append to a File")
            print("5. Back to Main Menu")
            print("---------------------------------")

            choice = int(input("Enter your File Operation Menu: "))

            if choice == 1:
                filename = input("Enter file name to create: ")
                try:
                    with open(filename, "x") as file:
                        print("\nFile created successfully!\n")
                except FileExistsError:
                    print("\nFile already exists!\n")

            elif choice == 2:
                filename = input("Enter file name to write: ")
                content = input("Enter data to write: ")
                with open(filename, "w") as file:
                    file.write(content)
                print("\nData written successfully!\n")

            elif choice == 3:
                filename = input("Enter file name to read: ")
                try:
                    with open(filename, "r") as file:
                        print("\nFile Content:")
                        print(file.read(), "\n")
                except FileNotFoundError:
                    print("\nFile not found!\n")

            elif choice == 4:
                filename = input("Enter file name to append: ")
                content = input("Enter data to append: ")
                with open(filename, "a") as file:
                    file.write("\n" + content)
                print("\nData appended successfully!\n")

            elif choice == 5:
                break

            else:
                print("\nInvalid option! Please try again.\n")

    def explore_module(self):
        module_name = input("Enter module name to explore: ")
        try:
            module = __import__(module_name)
            attributes = dir(module)
            print(f"\nAttributes in module '{module_name}':")
            print(attributes[:20], "...")  # Show only first 20 for brevity
            print("\n")
        except ModuleNotFoundError:
            print("\nModule not found!\n")


# ------------------ Main Program ------------------

toolkit = MultiUtilityToolkit()

print("=======================================")
print("   Welcome to Multi-Utility Toolkit    ")
print("=======================================")

while True:
    print("\n===== Main Menu =====")
    print("1. Datetime & Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")
    print("----------------------")

    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        toolkit.datetime_operations()

    elif main_choice == 2:
        toolkit.math_operations()

    elif main_choice == 3:
        toolkit.random_operations()

    elif main_choice == 4:
        toolkit.generate_uuid()

    elif main_choice == 5:
        toolkit.file_operations()

    elif main_choice == 6:
        toolkit.explore_module()

    elif main_choice == 7:
        print("Thank you for using the Multi-Utility Toolkit!")
        print("Goodbye!\n")
        break

    else:
        print("\nInvalid option! Please try again.\n")
