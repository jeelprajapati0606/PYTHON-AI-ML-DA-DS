import datetime
import os

class JournalManager:

    def __init__(self, file_name="journal.txt"):
        self.file_name = file_name

    # 1. Add Entry
    def add_entry(self):
        try:
            journal_entry = input("\nEnter your journal entry: ")

            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

            with open(self.file_name, "a") as file:
                file.write(f"{formatted_time} - {journal_entry}\n")

            print("\nEntry added successfully!")

        except Exception as error:
            print("Error:", error)

    # 2. View Entries
    def view_entries(self):
        try:
            print("\nYour journal entries:")
            print("----------------------")

            with open(self.file_name, "r") as file:
                entries = file.readlines()

                if not entries:
                    print("No entries found.")
                else:
                    for entry in entries:
                        print(entry.strip())

        except FileNotFoundError:
            print("\nOutput:")
            print("Journal file does not exist.")

    # 3. Search Entry
    def search_entry(self):
        keyword = input("\nEnter keyword or date to search: ")

        try:
            with open(self.file_name, "r") as file:
                entries = file.readlines()

            found = False
            print("\nMatching entries:")
            print("------------------")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry.strip())
                    found = True

            if not found:
                print(f"No entry found for keyword: {keyword}")

        except FileNotFoundError:
            print("Journal file not found.")

    # 4. Delete All Entries
    def delete_all_entries(self):
        try:
            with open(self.file_name, "r") as file:
                print("\nCurrent entries:")
                print(file.read())

            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")

            if confirm.lower() == "yes":
                open(self.file_name, "w").close()
                print("All journal entries deleted successfully.")
            else:
                print("Deletion cancelled.")

        except FileNotFoundError:
            print("No journal file found to delete.")

    # 5. Handle File Not Found
    def handle_file_error(self):
        try:
            with open("wrong_file.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("\nOutput:")
            print("Error: The journal file does not exist. Please add an entry first.")

    # 6. Invalid Option
    def invalid_option(self):
        print("\nOutput:")
        print("Invalid option. Please select a valid option from the menu.")


# -------- MAIN PROGRAM -------- #

journal = JournalManager()

print("Welcome to Personal Journal Manager!")

while True:
    print("\nPlease select an option:")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Handle file not found error")
    print("6. Invalid option")
    print("7. Exit")

    try:
        user_choice = int(input("User input: "))

        if user_choice == 1:
            journal.add_entry()

        elif user_choice == 2:
            journal.view_entries()

        elif user_choice == 3:
            journal.search_entry()

        elif user_choice == 4:
            journal.delete_all_entries()

        elif user_choice == 5:
            journal.handle_file_error()

        elif user_choice == 6:
            journal.invalid_option()

        elif user_choice == 7:
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        
        else:
            journal.invalid_option()

    except ValueError:
        print("Please enter a valid number.")
