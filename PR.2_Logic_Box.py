print()
print("Welcome To The Pattern Generator And Number Analyzer!")

print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")

while True:
    print()
    print("Select An Option: ")

    print("1. Generate A Pattern")
    print("2. Analyze A Range Of Numbers")
    print("3. Exit")
    print()

    a=int(input("Enter Your Choice: "))
   

    if a==1:
        b=int(input("Enter The Number Of Rows For The Pattern: "))
        for i in range(1, b+1):
            for j in range(i):
                print("*",end="")
            print()

    elif a==2:
        print()

        x=int(input("Enter The Start Of The Range: "))
        y=int(input("Enter The End Of The Range: "))
        
        print()
        sum=0
        for i in range(x,y+1):
            if i%2==0:
                print(f"number {i} is Even")
            else:
                print(f"number {i} is Odd ")

            
            sum+=i
        print()
        print(f"Sum Of All Numbers From {x} To {y} Is: {sum}")

        print()
    elif a==3:
        print("Exiting The Program. Goodbye!")

        break
    
    else:
        print("Invalid Input! Please Enter Option 1 To 3.")
        


            
    



