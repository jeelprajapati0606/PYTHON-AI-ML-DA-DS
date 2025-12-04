print("Welcome to the Data Analyzer and Transformer Program.")

print("----------------------------------------------------")

l=[]   
while True:
    
    print("\n********* Main Menu: *********")

    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    print()

    a=int(input("Please enter your choice: "))
    print()
    
   
# 1.input data:
    if a==1:
        
        b=input("Enter data for a 1D array (seprated by spaces): ")

        x= b.split()
        l= [int(c) for c in x]
        
        print()
        print("Data Has Been Stored Successfully!")
        print("-----------------------------------------------------")


#2. display data summary(built in function)

    elif a==2:
        print("\nData Summary:")
        total=len(l)
        print("Total elements:",total)

        minimum=min(l)
        print("Minimum value: ",minimum)

        maximum=max(l)
        print("Maximum value: ",maximum)

        s=sum(l)
        print("Sum of all values: ",s)

        average=sum(l)/len(l)
        print("Average value: ",average)

        print("-----------------------------------------------------")

# 3. calculate factorial by recursion.
    elif a==3:
        num=int(input("Enter a number to calculate its factorial: "))

        def fact(num):
         # use __doc__ string:
            """\nThis Question Finds The Factorial Of Given Number.   
    Parameters:
        num(int): Take Number From User By Input.
    return:
        int: Factorial Of Numbers."""
            
            print("\n Calculate Factorial: ")
        
            if num==1:
                return 1

            else:
                return num*fact(num-1)
        print(f"factorial of {num} is:",fact(num))
        print(fact.__doc__)

        print("-----------------------------------------------------")

# 4. Filter Data by Threshold use Lambda Function:
    
    elif a==4:
        print("\n Filter data by threshold:")

        data=int(input("Enter a threshold value to filter data above this value: "))

        value=list(filter(lambda n:n >= data,l ))
        print(f"filter Data (values >= {data})",value)

        print("-----------------------------------------------------")
    
# 5. sort data Ascending or Discending :

    elif a==5:
        if not l:
            print("You Have To Enter List First (Choose 1)!")
        
        else:
            print("1.Ascending")
            print("2.Discending")
            sort_data=int(input("Choose Sorting Option:"))
        
            if sort_data==1:
                l.sort()           # Ascending Order
                print("Sorted Data in Ascending Order:",l)
                print("-----------------------------------------------------")
            elif sort_data==2:
                l.sort(reverse=True) # Discending Order
                print("Sorted Data in Discending Order:",l)
                print("-----------------------------------------------------")
            else:
                print("Invalid Input!")

            print("-----------------------------------------------------")
        
# 6. Display Dataset Statistics (Return Multiple Values):

    elif a==6:
        print("Dataset Statistics: ")
        

        def big():           # maximum value
            """\nThis Question Finds The Maximum, Minimum,Average Of Data Given By User.""" 
            
            gr = l[0]        #start with first number
            for a in l:
                if a > gr:
                    gr=a
            print("-Maximum Value:",gr)
        big()
       
        


        def mini():         # minimum value
            less = l[0]     #start with first number
            for a in l:
                if a< less:
                    less=a
            print("-Minimum Value:",less)
        mini()

        def s():             #sum find
            global sum       # global use
            sum=0
            for a in l:
                sum+=a
            print("-Sum Of All Values:",sum)
        s()

        def average():       # average find
            count=0
            for a in l:
                count+=1

            av=sum/count
            print("-Average Value: ",av)
        average()
        print(big.__doc__)                    # __doc__use.

        print("------------------------------------------------------------")

# 7. Exit Program
    elif a==7:
        print("Thank You For Using Data Analyzer And Transformer Program. Goodbye!")
        print("-------------------------------------------------------------------")

# 8. invalid input
    else:
        print("***Invalid Input!*** Please Enter A Number Between 1 To 7.")
        print("------------------------------------------------------------")

            













        


    



        


        



