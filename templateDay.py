import numpy as np

def dayX_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        print(line)

def dayX_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        print(line)


day = "4"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# dayX_1(testFile)
# dayX_1(realFile)

# dayX_2(testFile)
# dayX_2(realFile)
