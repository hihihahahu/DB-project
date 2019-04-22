def printCrimeRate(result):
    # header
    print("-" * 125)
    print("{:25s}{:25s}{:25s}{:25s}{:25s}".format('county', 'year', 'violent crime rate', 'property crime rate', 'index crime rate'))
    print("-" * 125)
    # content
    for entry in result:
        for item in entry:
            print("{:25s}".format(str(item) + " "), end="")
        print("")
    # footer line
    print("-" * 125)