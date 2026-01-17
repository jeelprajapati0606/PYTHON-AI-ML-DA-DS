# Project Details / Description:

# You are required to build a simple personal finance management tool.
# The program should allow the user to:

# Add an expense with details like date, category, description, and amount.

#  View all recorded expenses in a clean format.

#  Calculate total spending so far.

#  Exit the program gracefully when the user chooses to.

# All tasks must be implemented using loops, if-else, lists, and dictionaries
# only. No user-defined functions or file handling should be used.


expenses = []
print("Welcome to Expence Tracker 💸")
while True:
    print("\n======= Menu ======= ")
    print("\n1. Add Expences")
    print("2. View All Expences")
    print("3. View Total Spending")
    print("4. Exit")

    print("======================")
    choice = int(input("Enter Your Choice (1-4): "))



    if choice == 1:
        print("\n-------Add Expenses-------")
        date = input("Enter Date (DD-MM-YYYY): ")

        category = input("Enter Category (Food, Travel, Shopping etc...: )")

        d = input("Enter Short Discription: ")

        amount = float(input("Enter Your Amount(₹): "))

        expense ={
            "Date" : date,
            "Category" : category,
            "discription" : d,
            "amount" : amount

        }

        expenses.append(expense)

        print("\n Expences Added Successfully!")

    elif choice == 2:
        print("\n-----View All Expenses---- ")
        if not expenses:
            print("Please add Expences...")

        else:
            for i in expenses:
                
                count = 1
                print(f"number :{count} -> {i["Date"]}, {i["Category"]}, {i["discription"]}, {i["amount"]}.  ")
                count=count+1

    elif choice == 3:
        print("\n===Total All Expenses===")

        total = 0
        for i in expenses:
            total = total + i["amount"]
        print("Total Expenses = ",total)

    elif choice == 4:
        print("Thankyou for use this system,Have A Nice Day Goodbye!")
        break

    else:
        print("Invalid Input! Please Enter Option (1 to 4)")










