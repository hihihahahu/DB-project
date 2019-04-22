def printCrimeRate(result):
    # header
    print("-" * 125)
    print("{:25s}{:25s}{:25s}{:25s}{:25s}".format('County', 'Year', 'Violent Crime Rate', 'Property Crime Rate', 'Index Crime Rate'))
    print("-" * 125)
    # content
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 125)

def printCrimeCount(result):
    # header
    print("-" * 125)
    print("{:25s}{:25s}{:25s}{:25s}{:25s}".format('County', 'Year', 'Violent Crime Count', 'Property Crime Count', 'Index Crime Count'))
    print("-" * 125)
    # content
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 125)

def printUnemploymentRate(result):
    print("-" * 75)
    print("{:25s}{:25s}{:25s}".format('County', 'Year', 'Unemployment Rate'))
    print("-" * 75)
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 75)

def printComparison(result):
    # header
    print("-" * 150)
    print("{:25s}{:25s}{:25s}{:25s}{:25s}{:25s}".format('County', 'Year', 'Violent Crime Rate', 'Property Crime Rate', 'Index Crime Rate', 'Unemployment Rate'))
    print("-" * 150)
    # content
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 150)
    
    
    
def printPopulation(result):
    print("-" * 75)
    print("{:25s}{:25s}{:25s}".format('County', 'Year', 'Population'))
    print("-" * 75)
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 75)

def printPopulation(result):
    print("-" * 75)
    print("{:25s}{:25s}{:25s}".format('County', 'Year', 'Population'))
    print("-" * 75)
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 75)
