print("welcome to the interactive personal data collector!")
print ()

Name = input("enter your name:")
Name = str(Name)

Age = input("enter your age:")
Age = int(Age)

Height = input("enter your height (in cm):")
Height = float(Height)

Favourite_number = input("enter your favourite number :")
favourite_number = int(Favourite_number)
print()

print("Thank You! Here is the information we collected:")
print()

print("Name:",Name ,"(Type:",type(Name),",Memory Address:", id(Name), ")")

print("Age:",Age ,"(Type:",type(Age),",Memory Address:", id(Age), ")")

print("Height:",Height ,"(Type:",type(Height),",Memory Address:", id(Height), ")")

print("Favourite Number:",Favourite_number ,"(Type:",type(favourite_number),",Memory Address:", id(Favourite_number), ")")
print()

current_year= 2025
Birth_year = current_year-Age
print("your birth year is approximately:",Birth_year,"( based on your age of ",Age,")")
print()
print("Thank You for using the Personal Data Collector. Goodbye!")
