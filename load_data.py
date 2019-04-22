import psycopg2
import csv
import pandas
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def main():
    
    conn = psycopg2.connect("host=localhost dbname=postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS project_db;")
    cur.execute("CREATE DATABASE project_db;")
    cur.execute(open("db_setup.sql","r").read())
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(open("create_schema.sql", "r").read())

    unemployment_stat = pandas.read_csv('Local_Area_Unemployment_Statistics__Beginning_1976.csv')
    unemployment_stat.shape
    unemployment_stat.drop_duplicates(keep = False, inplace = True)
    unemployment_stat.drop(['Labor Force', 
    #there's a ton of spaces in the column name in the original csv file
    #don't attempt to fix the syntax, it ain't wrong
    'Unemployment Rate                                                                                                                                                                      ']
    , axis = 1, inplace = True)
    unemployment_stat.to_csv('UnemploymentStat.csv', index=False)

    with open("UnemploymentStat.csv","r") as f:
        next(f)
        cur.copy_from(f, "UnemploymentStat", sep = ",")

    crime_stat = pandas.read_csv('Index_Crimes_by_County_and_Agency__Beginning_1990.csv')
    crime_stat.shape
    crime_stat.fillna(0, inplace = True)
    crime_stat.drop_duplicates(subset = ['County', 'Agency', 'Year'], keep = False, inplace = True)
    crime_stat.drop(['Months Reported', 'Index Total', 'Violent Total', 'Property Total'], axis = 1, inplace = True)
    crime_stat.to_csv('CrimeStat.csv', index=False, float_format = '%.0f')

    with open("CrimeStat.csv","r") as f:
        next(f)
        cur.copy_from(f, "CrimeStat", sep = ",")
    
    population = pandas.read_csv('Index__Violent__Property__and_Firearm_Rates_By_County__Beginning_1990.csv')
    population.shape
    population.fillna(0, inplace = True)
    population.drop_duplicates(keep = False, inplace = True)
    population.drop(['Index Rate', 'Index Count', 'Violent Rate','Violent Count', 'Property Rate', 'Property Count', 'Firearm Rate', 'Firearm Count'], axis = 1, inplace = True)
    population.to_csv('Population.csv', index=False, float_format = '%.0f')

    with open("Population.csv", "r") as f:
        next(f)
        cur.copy_from(f, "Population", sep = ",")
        
if __name__ == "__main__":
    main()
    
