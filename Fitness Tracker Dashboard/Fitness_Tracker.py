print("==================== Welcome to Fitness Tracker Application...! ====================")

# Import Numpy,Pandas,matplotlib, Seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#-------------- Fitness Tracker --------------

class Fitness_Tracker:
    def __init__(self, Fitness_Tracker='fitness_activities.csv'):
        self.Fitness_Tracker = Fitness_Tracker
        self.data = None


#--------------  Function to load and clean dataset --------------

    def load_data(self):
        print("\n== LOADING DATA ==")
        self.data = pd.read_csv(self.Fitness_Tracker)
        self.data.fillna(0, inplace=True)
        self.data['Date'] = pd.to_datetime(self.data['Date'])

        print("\nData loaded successfully!")


# --------------  User Input And Add Activity --------------

    def Add_Activity(self):
        print("\n== ADD ACTIVITY ==")
        date = input("Enter Date(YYYY-MM-DD): ")
        activity = input("Enter Activity Type (Running/Yoga/Cycling): ")
        duration = int(input("Enter Duration (Minutes): "))
        calories = int(input("Enter Calories Burned: "))

        new_data = {
            "Date": pd.to_datetime(date),
            "Activity Type": activity,
            "Duration (Minutes)": duration,
            "Calories Burned": calories
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_data])], ignore_index=True)
        print("\nActivity added successfully...!")

    
    # -------------- Calculate metrics using NumPy --------------

    def Calculate_Matrics(self):
        print("\n== FITNESS METRICS ==")
        total_calories = np.sum(self.data['Calories Burned'])
        avg_duration = np.mean(self.data['Duration (Minutes)'])
        print("Total Calories Burned :", total_calories)
        print("Average Duration :", round(avg_duration, 2), "minutes")
        
        print("\nFitness Matrix Added...!")

    # -------------- Filter activity --------------

    def Filter_Activities(self):
        print("\n== FILTER ACTIVITY ==")
        activity = input("\nEnter activity to filter: ")
        filtered = self.data[self.data['Activity Type'] == activity]
        print("\nFiltered Data:\n",filtered)
        

        print("\nFilter Activity Updated...! ")

    
    # -------------- Visualization --------------

    def visualize_data(self):
        print("\n== DATA VISUALIZATION == ")
        

        #-------------- Bar Chart --------------

    def plot_bar(self):
        plt.figure()
        self.data.groupby('Activity Type')['Duration (Minutes)'].sum().plot(kind='bar')
        plt.title("Total Time Spent per Activity")
        plt.xlabel("Activity Type")
        plt.ylabel("Minutes")
        plt.show()
        print("\n---Bar Chart Displayed---")

        #-------------- Line Graph --------------

    def plot_line(self):
        plt.figure()
        plt.plot(self.data['Date'], self.data['Calories Burned'], marker='o', linewidth=2, color='red')
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.show()

        print("\n---Line Graph Displayed---")

        #-------------- Pie Chart --------------

    def plot_pie(self):
        plt.figure()
        self.data['Activity Type'].value_counts().plot(kind='pie', autopct='%1.1f%%',color='skyblue')
        plt.title("Activity Distribution")
        plt.ylabel("frequancy")
        plt.show()

        print("\n---Pie Chart Displayed---")

        #-------------- Heatmap --------------

    def plot_heatmap(self):
        plt.figure()
        sns.heatmap(self.data[['Duration (Minutes)', 'Calories Burned']].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

        print("\n---Heatmap Displayed---")
    

def main():
        tracker = Fitness_Tracker()
        tracker.load_data()

        while True:
            print("\n===================== Fitness Tracker Menu =====================")
            print("1. Add New Activity")
            print("2. Calculate Metrics")
            print("3. Filter Activity")
            print("4. Show Visualizations")
            print("5. Exit")

            choice = input("Enter Your Choice: ")

            if choice == '1':
                tracker.Add_Activity()

            elif choice == '2':
                tracker.Calculate_Matrics()

            elif choice == '3':
                tracker.Filter_Activities()


            elif choice == '4':
                print("\n== VISUALIZATIONS ==")
                print("1. Bar Chart")
                print("2. Line Chart")
                print("3. Pie Chart")
                print("4. Heatmap")
                print("5. All Charts")
                option = input("Enter Graph Option (1-5): ")

                if option == '1':
                    tracker.plot_bar()
                elif option == '2':
                    tracker.plot_line()
                elif option == '3':
                    tracker.plot_pie()
                elif option == '4':
                    tracker.plot_heatmap()
                elif option == '5':
                    tracker.visualize_data()
                else:
                    print("Invalid option. Please enter 1-5.")

                break

            elif choice == '5':
                print("Exiting Fitness Tracker. Goodbye....!")

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
                 

                






    

        