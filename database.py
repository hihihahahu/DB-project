import psycopg2
import psycopg2.extras
import csv
import pandas
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql

def GetCrimeRateOfYear(county, year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    #sprint("year: " + year)
    cur.execute(sql.SQL("SELECT * FROM {} WHERE LOWER({}) = %s AND {} = %s;").format(sql.Identifier('crimerate'), sql.Identifier('county'), sql.Identifier('year')), (county, year, ))
    result = cur.fetchall()
    #print(result)
    return result
    
def GetCrimeRate(county):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

def GetCrimeRateAll(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    if sort_selection == '1':
        cur.execute("SELECT * FROM CrimeRate WHERE LOWER(County) = %s ORDER BY Year DESC", [county])
    else:
        cur.execute("SELECT * FROM CrimeRate WHERE LOWER(County) = %s ORDER BY IndexRate DESC", [county])
    result = cur.fetchall()
    return result

def GetCrimeCountAll(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    if sort_selection == '1':
        cur.execute("SELECT * FROM CrimeRate WHERE LOWER(County) = %s ORDER BY Year DESC", [county])
    else:
        cur.execute("SELECT * FROM CrimeRate WHERE LOWER(County) = %s ORDER BY IndexRate DESC", [county])
    result = cur.fetchall()
    return result