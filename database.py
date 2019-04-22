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

def GetCrimeRateOfAllCounties(year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {} WHERE {} = %s ORDER BY IndexRate DESC;").format(sql.Identifier('crimerate'), sql.Identifier('year')), (year, ))
    result = cur.fetchall()
    return result


    
def GetCrimeCountOfYear(county, year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    #sprint("year: " + year)
    cur.execute(sql.SQL("SELECT county, year, sum(violenttotal), sum(propertytotal), sum(indextotal) FROM {} WHERE LOWER({}) = %s AND {} = %s GROUP BY county, year;").format(sql.Identifier('crimetotal'), sql.Identifier('county'), sql.Identifier('year')), (county, year, ))
    result = cur.fetchall()
    #print(result)
    return result

def GetCrimeCountAll(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    if sort_selection == '1':
        cur.execute("SELECT county, year, sum(violenttotal), sum(propertytotal), sum(indextotal) FROM CrimeTotal WHERE LOWER(County) = %s GROUP BY county, year ORDER BY Year DESC", [county])
    else:
        cur.execute("SELECT county, year, sum(violenttotal), sum(propertytotal), sum(indextotal) AS indextotal2 FROM CrimeTotal WHERE LOWER(County) = %s GROUP BY county, year ORDER BY indextotal2 DESC", [county])
    result = cur.fetchall()
    return result

def GetCrimeCountOfAllCounties(year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT county, year, sum(violenttotal), sum(propertytotal), sum(indextotal) AS indextotal2 FROM {} WHERE {} = %s GROUP BY county, year ORDER BY indextotal2 DESC;").format(sql.Identifier('crimetotal'), sql.Identifier('year')), (year, ))
    result = cur.fetchall()
    return result



def GetUnemploymentRateAll(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    county = county + " county"
    if sort_selection == '1':
        cur.execute("SELECT * FROM unemploymenttable WHERE LOWER(county) = %s ORDER BY year DESC", [county])
    else:
        cur.execute("SELECT * FROM unemploymenttable WHERE LOWER(county) = %s ORDER BY unemploymentrate DESC", [county])
    result = cur.fetchall()
    return result

def GetUnemploymentRateOfYear(county, year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    county = county + " county"
    cur.execute(sql.SQL("SELECT * FROM {} WHERE LOWER({}) = %s AND {} = %s;").format(sql.Identifier('unemploymenttable'), sql.Identifier('county'), sql.Identifier('year')), (county, year, ))
    result = cur.fetchall()
    return result

def GetUnemploymentRateOfAllCounties(year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    #cur.execute("SELECT * FROM unemploymenttable WHERE LOWER(county) LIKE %s AND year = %s ORDER BY unemploymentrate DESC", ('%' + ' County',year, ))
    cur.execute(sql.SQL("SELECT * FROM {} WHERE LOWER({}) LIKE %s AND {} = %s ORDER BY unemploymentrate DESC;").format(sql.Identifier('unemploymenttable'), sql.Identifier('county'), sql.Identifier('year')), ('% county', year, ))
    result = cur.fetchall()
    return result



def GetComparisonAll(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    if sort_selection == '1': # sort by year
        cur.execute("SELECT * FROM Comparison WHERE LOWER(County) = %s ORDER BY Year DESC", [county])
    elif sort_selection == '2': # sort by unemployment rate (descending)
        cur.execute("SELECT * FROM Comparison WHERE LOWER(County) = %s ORDER BY UnemploymentRate DESC", [county])
    else: # Sort by index crime rate (descending)
        cur.execute("SELECT * FROM Comparison WHERE LOWER(County) = %s ORDER BY IndexRate DESC", [county])
    result = cur.fetchall()
    return result

def GetComparisonOfYear(county, year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {} WHERE LOWER({}) = %s AND {} = %s;").format(sql.Identifier('comparison'), sql.Identifier('county'), sql.Identifier('year')), (county, year, ))
    result = cur.fetchall()
    return result

def GetComparisonOfAllCounties(year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {} WHERE {} = %s ORDER BY IndexRate DESC;").format(sql.Identifier('comparison'), sql.Identifier('year')), (year, ))
    result = cur.fetchall()
    return result


def GetPopulationALL(county, sort_selection):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    if sort_selection == '1':
        cur.execute("SELECT * FROM Population WHERE LOWER(County) = %s ORDER BY Year DESC", [county])
    else:
        cur.execute("SELECT * FROM Population WHERE LOWER(County) = %s ORDER BY Population DESC", [county])
    result = cur.fetchall()
    return result

def GetPopulationOfYear(county, year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {} WHERE LOWER({}) = %s AND {} = %s;").format(sql.Identifier('population'), sql.Identifier('county'), sql.Identifier('year')), (county, year, ))
    result = cur.fetchall()
    return result

def GetPopulationOfAllCounties(year):
    conn = psycopg2.connect(host='localhost', dbname='project_db', user='db_project', password='db_project')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {} WHERE {} = %s ORDER BY Population DESC;").format(sql.Identifier('population'), sql.Identifier('year')), (year, ))
    result = cur.fetchall()
    return result

