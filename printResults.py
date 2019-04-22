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
    print("{:25s}{:25s}{:25s}".format('county', 'year', 'unemployment rate'))
    print("-" * 75)
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end='')
        print("")
    print("-" * 75)