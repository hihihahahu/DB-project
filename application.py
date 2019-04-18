import psycopg2
import csv
import pandas
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from database import GetCrimeRateOfYear

def main():
    while True:
        user_input = input("Enter a county name (case insensitive), \"all\" for all counties, or \"exit\" to exit: ")
        #remove tailing and leading spaces
        user_input = user_input.strip()
        #convert to lowercase letters
        user_input = user_input.lower()
        if user_input == 'exit':
            break
        if user_input == 'all':
            #to be implemented
            break
        else:
            while True:
                #1. crime rate stats
                #2. crime count stats
                #3. unemployment rate stats
                #4. population stats
                #5. crime rate vs. unemployment rate
                print("Your selected county is: " + user_input + "\n")
                user_input2 = input("Select an option from below (enter the corresponding number):\n" + 
                "\t1: Explore crime rate statistics\n" + 
                "\t2: Explore crime count statistics\n" +
                "\t3: Explore unemployment rate statistics\n" +
                "\t4: Explore population statistics\n" + 
                "\t5: Explore crime rate vs. unemployment rate\n" +
                "\t6: quit\n")
                if user_input2 == '1':
                    #crime rate
                    while True:
                        year = input("Select a year from 1990 to 2018, or enter \"all\" to view data of all years, " + 
                        "or \"quit\" to exit: ")
                        year = year.strip()
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option:\n" +
                                "\t1: Sort by year (descending)\n" +
                                "\t2: Sort by crime rate (descending)\n")
                                if sort_selection == '1':
                                    #display results: crime rates of a county (all years), sorted by year
                                    break
                                elif sort_selection == '2':
                                    #display results: crime rates of a county (all years), sorted by rates
                                    break
                                else:
                                    print("Invalid input.\n")
                        elif year == 'quit':
                            break
                        else:
                            try:
                                val = int(year)
                                #user has selected a single county, specified year & data type (crime rate), find and print the row
                                result = GetCrimeRateOfYear(user_input, val)
                                print("{:25s}{:25s}{:25s}{:25s}{:25s}".format('county', 'year', 'violent crime rate', 'property crime rate', 'index crime rate'))
                                for entry in result:
                                    for item in entry:
                                        print("{:25s}".format(str(item) + " "), end = '')
                                    #print("\n")
                                print("\n")
                                break
                            except ValueError:
                                print("Invalid input.\n")
                            
                elif user_input2 == '2':
                    #crime count
                    break
                elif user_input2 == '3':
                    #unemployment rate
                    break
                elif user_input2 == '4':
                    #population
                    break
                elif user_input2 == '5':
                    #crime rate vs. unemployment rate
                    break
                elif user_input2 == '6':
                    break
                else:
                    print("Invalid input.\n")
                

if __name__ == "__main__":
    main()

