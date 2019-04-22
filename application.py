import psycopg2
import csv
import pandas
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from database import GetCrimeRateOfYear, GetCrimeRateAll
from database import GetCrimeCountOfYear, GetCrimeCountAll
from database import GetUnemploymentRateAll, GetUnemploymentRateOfYear, GetUnemploymentRateOfAllCounties
from database import GetComparisonAll, GetComparisonOfYear
from database import GetPopulationALL, GetPopulationOfYear
from printResults import printCrimeRate, printUnemploymentRate, printCrimeCount, printComparison, printPopulation

def main():
    while True:
        county = input("Enter a county name (case insensitive), \"all\" for all counties, or \"exit\" to exit: ")
        #remove tailing and leading spaces
        county = county.strip()
        #convert to lowercase letters
        county = county.lower()
        if county == 'exit':
            break
        if county == 'all':
            while True:
                user_input2 = input("Select an option from below (enter the corresponding number):\n" +
                                    "\t1: Explore crime rate statistics\n" +
                                    "\t2: Explore crime count statistics\n" +
                                    "\t3: Explore unemployment rate statistics\n" +
                                    "\t4: Explore population statistics\n" +
                                    "\t5: Explore crime rate vs. unemployment rate\n" +
                                    "\t6: quit\n")
                if user_input2 == '1':
                    while True:
                        year = input("Select a year from 1990 to 2017, " +
                                            "or \"quit\" to exit: ")
                        try:
                            year_val = int(year)
                            print("results will be sorted by crime rate, in descending order")
                            result = GetCrimeRateOfAllCounties(year_val)
                            printCrimeRate(result)
                        except ValueError:
                            print("Invalid input.\n")
                elif user_input2 == '2':
                    while True:
                        year = input("Select a year from 1990 to 2017, " +
                                            "or \"quit\" to exit: ")
                        try:
                            year_val = int(year)
                            print("results will be sorted by crime count, in descending order")
                            # user has selected a single county, specified year & data type (crime rate), find and print the row
                            result = GetCrimeCountOfAllCounties(year_val)
                            printCrimeCount(result)
                        except ValueError:
                            print("Invalid input.\n")
                elif user_input2 == '3':
                    while True:
                        year = input("Select a year from 1990 to 2017, " +
                                            "or \"quit\" to exit: ")
                        try:
                            year_val = int(year)
                            print("results will be sorted by unemployment rate, in descending order")
                            # user has selected a single county, specified year & data type (crime rate), find and print the row
                            result = GetUnemploymentRateOfAllCounties(year_val)
                            printUnemploymentRate(result)
                        except ValueError:
                            print("Invalid input.\n")

                elif user_input2 == '4':
                     while True:
                        year = input("Select a year from 1990 to 2017, " +
                                            "or \"quit\" to exit: ")
                        try:
                            year_val = int(year)
                            print("results will be sorted by population, in descending order")
                            # user has selected a single county, specified year & data type (crime rate), find and print the row
                            result = GetPopulationOfAllCounties(year_val)
                            printPopulation(result)
                        except ValueError:
                            print("Invalid input.\n")
                elif user_input2 == '5':
                    while True:
                        year = input("Select a year from 1990 to 2017, " +
                                            "or \"quit\" to exit: ")
                        try:
                            year_val = int(year)
                            print("results will be sorted by index crime rate, in descending order")
                            # user has selected a single county, specified year & data type (crime rate), find and print the row
                            result = GetComparisonOfAllCounties(year_val)
                            printComparison(result)
                        except ValueError:
                            print("Invalid input.\n")
                elif user_input2 == '6':
                    break
            break
        else:
            while True:
                #1. crime rate stats
                #2. crime count stats
                #3. unemployment rate stats
                #4. population stats
                #5. crime rate vs. unemployment rate
                print("Your selected county is: " + county + "\n")
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
                        year = input("Select a year from 1990 to 2017, or enter \"all\" to view data of all years, " +
                        "or \"quit\" to exit: ")
                        # remove tailing and leading spaces
                        year = year.strip()
                        # explore all years from 1990 to 2018
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option (enter the corresponding number):\n" +
                                "\t1: Sort by year (descending)\n" +
                                "\t2: Sort by index crime rate (descending)\n")

                                if sort_selection != '1' and sort_selection != '2':
                                    print("Invalid input.\n")
                                else:
                                    result = GetCrimeRateAll(county, sort_selection)
                                    printCrimeRate(result)
                                    break
                                    
                        elif year == 'quit':
                            break
                        else:
                            try:
                                year_val = int(year)
                                #user has selected a single county, specified year & data type (crime rate), find and print the row
                                result = GetCrimeRateOfYear(county, year_val)
                                printCrimeRate(result)
                            except ValueError:
                                print("Invalid input.\n")
                            
                elif user_input2 == '2':
                    #crime count
                    while True:
                        year = input("Select a year from 1990 to 2018, or enter \"all\" to view data of all years, " + 
                        "or \"quit\" to exit: ")
                        # remove tailing and leading spaces
                        year = year.strip()
                        # explore all years from 1990 to 2018
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option (enter the corresponding number):\n" +
                                "\t1: Sort by year (descending)\n" +
                                "\t2: Sort by index crime count (descending)\n")

                                if sort_selection != '1' and sort_selection != '2':
                                    print("Invalid input.\n")
                                else:
                                    result = GetCrimeCountAll(county, sort_selection)
                                    printCrimeCount(result)
                                    break
                        elif year == 'quit':
                            break
                        else:
                            try:
                                year_val = int(year)
                                #user has selected a single county, specified year & data type (crime rate), find and print the row
                                result = GetCrimeCountOfYear(county, year_val)
                                printCrimeCount(result)
                                break
                            except ValueError:
                                print("Invalid input.\n")

                elif user_input2 == '3':
                    while True:
                        year = input("Select a year from 1990 to 2019, or enter \"all\" to view data of all years, " +
                                     "or \"quit\" to exit: ")
                        year = year.strip()
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option (enter the corresponding number):\n" +
                                                       "\t1: Sort by year (descending)\n" +
                                                       "\t2: Sort by unemployment rate (descending)\n")

                                if sort_selection != '1' and sort_selection != '2':
                                    print("Invalid input.\n")
                                else:
                                    result = GetUnemploymentRateAll(county, sort_selection)
                                    printUnemploymentRate(result)
                                    break
                        elif year == 'quit':
                            break
                        else:
                            try:
                                year_val = int(year)
                                result = GetUnemploymentRateOfYear(county, year_val)
                                printUnemploymentRate(result)
                            except ValueError:
                                print("Invalid input.\n")


                elif user_input2 == '4':
                    while True:
                        year = input("Select a year from 1990 to 2019, or enter \"all\" to view data of all years, " +
                                     "or \"quit\" to exit: ")
                        year = year.strip()
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option (enter the corresponding number):\n" +
                                                       "\t1: Sort by year (descending)\n" +
                                                       "\t2: Sort by population (descending)\n")

                                if sort_selection != '1' and sort_selection != '2':
                                    print("Invalid input.\n")
                                else:
                                    result = GetPopulationALL(county, sort_selection)
                                    printPopulation(result)
                                    break
                        elif year == 'quit':
                            break
                        else:
                            try:
                                year_val = int(year)
                                result = GetPopulationOfYear(county, year_val)
                                printPopulation(result)
                            except ValueError:
                                print("Invalid input.\n")                   
                    #population
                    break
                elif user_input2 == '5':
                    #crime rate vs. unemployment rate
                    while True:
                        year = input("Select a year from 1990 to 2019, or enter \"all\" to view data of all years, " +
                                     "or \"quit\" to exit: ")
                        year = year.strip()
                        if year == 'all':
                            while True:
                                sort_selection = input("Select a sorting option (enter the corresponding number):\n" +
                                                       "\t1: Sort by year (descending)\n" +
                                                       "\t2: Sort by unemployment rate (descending)\n"
                                                       "\t3: Sort by index crime rate (descending)\n")

                                if sort_selection != '1' and sort_selection != '2' and sort_selection != '3':
                                    print("Invalid input.\n")
                                else:
                                    result = GetComparisonAll(county, sort_selection)
                                    printComparison(result)
                                    break
                        elif year == 'quit':
                            break
                        else:
                            try:
                                year_val = int(year)
                                result = GetComparisonOfYear(county, year_val)
                                printComparison(result)
                            except ValueError:
                                print("Invalid input.\n")
                elif user_input2 == '6':
                    break
                else:
                    print("Invalid input.\n")
                

if __name__ == "__main__":
    main()

