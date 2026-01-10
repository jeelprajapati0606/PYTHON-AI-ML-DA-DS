import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class sales_data:

    load_file = "sales_data.csv"
    salesData = pd.read_csv(load_file)
    
    load_file2 = "sales_data2.csv"
    salesData2 = pd.read_csv(load_file2)
    concat_data = pd.concat([salesData, salesData2], ignore_index=True)
    
    #-------------- load dataset -------------- 
    
    class load_Dataset:
        def __init__(self,csv_file):
            try:
                self.data = pd.read_csv(csv_file)
                print("Sales Data Loded Successfully..")

            except FileNotFoundError:
                print(f"Error: The File '{csv_file}' Was NOT Found...")
                self.data=None

            
            except pd.errors.EmptyDataError:
                print(print(f"Error: The File '{csv_file}' Is Empty..."))
                self.data=None

            except Exception as e:
                print(f"An Unexpected Error Occured While Loading The Data: {e}..")
                self.data=None

    #-------------- explore data -------------- 

    class explore_data:
        def __init__(self,data):
            self.data = data

    class DataFrame_Operation:
        def __init__(self,data):
            self.data = data

        def mathematical_operation(self):
            

            print("Sales Data2 Is Already Loded....")

            # Perform Mathematical Sales Data:

            Total_Sales=self.data['Total'] = self.data['Quantity'] * self.data['Profit']
            print(f"Total Sales:\n{Total_Sales.head()}")

            #Apply 10% Discount
            Discount = self.data['Discounted_price'] = self.data['Profit'] * 0.9
            print(f"\nDiscount:\n{Discount.head()}")

        def Combine_DataFrames(self):
            load_file2 = "sales_data2.csv"
            salesData2 = pd.read_csv(load_file2)

        # combine data
            concat_data = pd.concat([self.data, salesData2], ignore_index=True)
            print(f"\nCombine DataFrame :\n {concat_data}")

        def split_dataframes(self):

            #split data
            North_Sale = self.data[self.data["Region"] == "North"]
            print("Split By North Sale:\n",North_Sale)
            
            print("\nDataFrame Split By Region")

    #-------------- Clean data --------------

    class clean_data:

        def __init__(self, data):
            self.data = data

        def missing_rows(self):
           
            missing_rows = self.data[self.data.isnull().any(axis=1)]
            if missing_rows.empty:
                print("NO Missing Values Found In The Dataset..!")

            else:
                print("\nRows With Missing Values:\n",missing_rows)
    
        def fill_missing_mean(self):
            
            fill_values = self.data.fillna(self.data.mean(numeric_only=True))  
            
            print("\nFilling Missing Value With Mean:\n",fill_values)
    
        def dropna_missing(self):
            drop = self.data.dropna()
            print("Drop Row With Missing Value:\n",drop)

        def replace_missing(self,value=0):
            self.data = self.data.fillna(value)
            print("\nReplace Missing Value With :\n",value)

            print(self.data)

    #-------------- Statical Analysis --------------

    class statical_analysis:
        def __init__(self,data):
            self.data = data

        def statics(self):
            print("--- Describe ---")
            describe = self.data.describe()
            print("\nThe Describe Data:\n",describe)

        def std_dev(self):
            print("--- Standard Deviation ---")
            std = self.data.std(numeric_only=True)
            print("\nStadard devision:\n",std)

        def variance(self):
            print("--- Variance ---")
            varience = self.data.var(numeric_only=True)
            print("\nVarience Data:\n",varience)

        def percentile(self):
            print("--- Percentile ---")
            pr = self.data.quantile([0.25, 0.5, 0.75],numeric_only=True)
            print("\nPercentile Data:\n",pr)

    #-------------- Visualize data --------------

    class visualize_data:

        def __init__(self,data):
            self.data = data
            self.current_figure = None

        def bar_plot(self, x_column, y_column):
            print("\n== Bar Plot ==")
            fig = plt.figure(figsize=(10,6))
            plt.bar(self.data[x_column], self.data[y_column], color = 'red')

            
            plt.title("Bar Plot")
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.tight_layout()
            self.current_figure = fig
            plt.show()
            print("Bar Plot Displayed Successfully!")

        def line_plot(self, x_column, y_column):
            print("\n== Line Plot ==")
            fig = plt.figure(figsize=(10,6))
            plt.plot(self.data[x_column], self.data[y_column], color= 'blue', linestyle = '--', marker='o')
            plt.title("Line Plot")
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.tight_layout()
            self.current_figure = fig
            plt.show()
            print("Line Plot Displayed Successfully!")

        def scatter_plot(self, x_column, y_column):
            print("\n== Scatter Plot ==")
            fig = plt.figure(figsize=(10,6))

            plt.scatter(self.data[x_column], self.data[y_column],color= 'green')
            plt.title("Scatter Plot")
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(alpha=0.5)
            plt.tight_layout()
            self.current_figure = fig
            plt.show()
            print("Scatter Plot Displayed Successfully!")

        def pie_chart(self, label, value):
            fig = plt.figure(figsize=(10,6))
            self.data.groupby(label)[value].sum().plot(kind='pie',autopct='%1.1f%%')
            
            plt.title("Pie Chart")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()


            print("Pie Chart Displayed Successfully!")

        def histogram_plot(self, column):
            print("\n== Histogram Plot ==")
            fig = plt.figure(figsize=(10,6))

            plt.hist(self.data[column], bins=10, edgecolor='black')
            plt.title("Histogram Plot")
            
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

            print("Histogram Displayed Sucessfully!")

        def stack_plot(self, labels):
            print("\n== Stack Plot ==")
            fig = plt.figure(figsize=(10,6))

            grouped_data = self.data.groupby(labels).sum(numeric_only=True)
            grouped_data.plot(kind='area', stacked=True)
            
            plt.title("Stack Plot")
            plt.xlabel(labels)
            plt.ylabel("Values")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

            print("Stack Chart Displayed Successfully!")

        def seborn_heatmap(self, x_column, y_column):
            corr = self.data.corr(numeric_only=True)
            fig=plt.figure(figsize=(10, 6))
            
            sns.heatmap(corr,x_column, y_column, annot=True, cmap="YlGnBu", linewidths=0.5)
            plt.title("Heatmap Plot")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()
            print("Hetmap Plot Displayed Successfully!")

    #-------------- Svve data --------------
        def save_plot(self, filename):
            if self.current_figure is not None:
                self.current_figure.savefig(filename, dpi=300, bbox_inches='tight')
                print(f"Visualization Saved As {filename} Successfully!")

            else:
                print("Error: No Plot To Save. Please Create A Plot First (Option 6)")


                    
                    
                #-------------- Main Data Create -------------       
def main():
    analyzer = None

    # Create custom DataFrame with missing values for testing
    data = {
        "Date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05"],
        "Product": ["Mobile","Laptop","Chair","Table","Headphones"],
        "Region": ["North","South", np.nan,"East","North"],  # Missing
        "Sales": [25000,55000,7000,12000, np.nan],          # Missing
        "Profit": [5000,8000,1500,2500,800],
        "Quantity": [5,2,10,4,6]
    }
    df = pd.DataFrame(data)


    while True:
        print("\n============ Data Analysis & Visualization Program ============")
        print("Please Select An Option: ")
        print("1. Load DataSet")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        print("=====================================================================")

        option = input("Enter Your Choice: ")

        if option == '1':
            print("\n== Load Dataset ==")
            load_file = input("Enter The path Of The Dataset CSV file [sales_data.csv available]: ")
            analyzer = sales_data.load_Dataset(load_file)

        elif option == '2':
            print("\n== Explore Data == ")
            print("1. Display The First 5 Rows")
            print("2. Display The Last 5 Rows")
            print("3. Display Column Names")
            print("4. Display Data Types")
            print("5. Display Basic Info")

            choice = input("Enter Explore Data Choice: ")

            if analyzer is not None and analyzer.data is not None:
                explorer = sales_data.explore_data(analyzer.data)


                if choice == '1':
                    
                    print("\nFirst 5 Rows:\n",explorer.data.head())

                elif choice == '2':
                    
                    print("\nlast 5 rows:\n",explorer.data.tail())
                    
                elif choice == '3':
                    
                    print("Display Column:\n",list(explorer.data.columns))

                elif choice == '4':
                    
                    print("\nData Types:\n",explorer.data.dtypes)

                elif choice == '5':
                    
                    print("\n Display Info:\n",explorer.data.info())

                else:
                    print("\nInvalid Input!Please Enter Option 1 to 5...")
            else:
                print("NO Data Loded...Please Load The Data First...!")


        elif option == '3':
            print("\n== Perform DataFrame Operations ==")
            print("1. Perform Mathematical")
            print("2. Combine Multiple DataFrames")
            print("3. Split DataFrames")

            choice = input("Enter Perform DataFrame Operation Choice: ")

            if analyzer is not None and analyzer.data is not None:
                data_frame = sales_data.DataFrame_Operation(analyzer.data)

                if choice == '1':
                    print("Performing Mathematical Operation...")
                    data_frame.mathematical_operation()

                elif choice == '2':
                    print("Combine Multiple DataFrames...")

                    data_frame.Combine_DataFrames()

                elif choice  == '3':
                    print("\nSplit DataFrames...\n")

                    data_frame.split_dataframes()

                else:
                    print("\nInvalid Input!Please Enter Option 1 to 3...")

            else:
                print("NO Data Loded...Please Load The Data First...!")

        elif option == '4':
            print("\n== Handling Missing Data ==")
            print("1. Display Rows With Missing Values")
            print("2. Fill Missing Values With Mean")
            print("3. Drop Rows With Missing Values")
            print("4. Replace Missing Values With A Specific Value")

            choice = input("Enter Handle Missing Data Choice: ")

            # SalesData2 = pd.read_csv("sales_data2.csv")

            handle_missing_data = sales_data.clean_data(df)

            if choice == '1':
                    handle_missing_data.missing_rows()

            elif choice == '2':
                handle_missing_data.fill_missing_mean()

            elif choice == '3':
                handle_missing_data.dropna_missing()

            elif choice == '4':
                handle_missing_data.replace_missing(0)

            else:
                print("\nInvalid Input!Please Enter Option 1 to 4...")

        elif option == '5':
            print("\n== Generate Descriptive Statistics ==")

            print("1. Describe")
            print("2. Standard Deviation")
            print("3. Variance")
            print("4. Percentiles")

            choice = input("Enter Statical choice: ")

            if analyzer is not None and analyzer.data is not None:
                statical = sales_data.statical_analysis(analyzer.data)
                
                if choice == '1':
                    statical.statics()

                elif choice == '2':
                    statical.std_dev()

                elif choice == '3':
                    statical.variance()

                elif choice == '4':
                    statical.percentile()

                else:
                    print("\nInvalid Input!Please Enter Option 1 to 4...")

            else:
                print("NO Data Loded...Please Load The Data First...!")

        
        elif option == '6':
            print("\n== Data Visualization == ")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Seborn Heatmap")

            choice = input("Enter plot choice: ")
            
            if analyzer is not None and analyzer.data is not None:
                plot = sales_data.visualize_data(analyzer.data)

                analyzer.visualization = plot # store option 7
                print("\nAvailable columns:", list(analyzer.data.columns))
                print()

                if choice == '1':
                    
                    x = input("Enter X-axis Column Name: ")
                    y = input("Enter Y-axis Column Name: ")

                    plot.bar_plot(x, y)
                    plt.show()

                elif choice == '2':
                    
                    x = input("Enter X-axis Column Name: ")
                    y = input("Enter Y-axis Column Name: ")

                    plot.line_plot(x, y)
                    # plt.show()

                elif choice == '3':
                    x = input("Enter X-axis Column Name: ")
                    y = input("Enter Y-axis Column Name: ")

                    plot.scatter_plot(x, y)

                elif choice == '4':
                    label = input("Enter label Column Name: ")
                    value = input("Enter Value Column Name: ")

                    plot.pie_chart(label, value)

                elif choice == '5':
                    column = input("Enter The Column Name: ")
                    plot.histogram_plot(column)

                elif choice == '6':
                    label = input("Enter Labels Name: ")

                    plot.stack_plot(label)

                elif choice == '7':
                    
                    x = input("Enter X-axis Column Name: ")
                    y = input("Enter Y-axis Column Name: ")

                    plot.seborn_heatmap(x, y)

                else:
                    print("\nInvalid Input!Please Enter Option 1 to 7...")

            else:
                print("NO Data Loded...Please Load The Data First...!")
                    
        
        elif option == '7':
            print("\n== Save Visualization ==")

            if hasattr(analyzer, 'visualization') and analyzer.visualization is not None:
                filename = input("Enter The Filename To Save Plot [eg.sales_plot.png or jpeg]: ")

                if filename:
                    analyzer.visualization.save_plot(filename)

                else:
                    print("Invalid Filename! Please Try Again")

            else:
                print("No Plot To Save. Please Create A plot First (Option 6)")

        elif option == '8':
            print("\nExiting Program. Goodbye!")
            break

        else:
            print("\nInvalid Choice! Please Enter Option 1 to 8")

if __name__ == "__main__":
    main()          

        





        





