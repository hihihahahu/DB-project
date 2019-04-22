def printCrimeRate(result):
    print("{:25s}{:25s}{:25s}{:25s}{:25s}".format('county', 'year', 'violent crime rate', 'property crime rate', 'index crime rate'))
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("\n")
    print("\n")

def printUnemploymentRate(result):
    print("{:25s}{:25s}{:25s}".format('county', 'year', 'unemployment rate'))
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("\n")
    print("\n")