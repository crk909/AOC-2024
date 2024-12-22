import numpy as np

def day7_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    collections = 0
    for line in lines:
        goal, rest = line.split(":")
        goal = int(goal)
        values = [int(x) for x in rest.strip().split(" ")]
        possible = list()
        possible.append(values[0])
        for i in values[1:]:
            new_possibilities = []
            for v in possible:
                new_possibilities.append(v * i)
                new_possibilities.append(v + i)
            possible = new_possibilities
        if goal in possible:
            collections += goal
            print("Found ", goal, " in: ", possible)
        else:
            print("NOT Found ", goal, " in: ", possible)
    print(collections)

def day7_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    collections = 0
    for line in lines:
        goal, rest = line.split(":")
        goal = int(goal)
        values = [int(x) for x in rest.strip().split(" ")]
        possible = list()
        possible.append(values[0])
        for i in values[1:]:
            new_possibilities = []
            for v in possible:
                new_possibilities.append(v * i)
                new_possibilities.append(v + i)
                new_possibilities.append(int(str(v) + str(i)))
            possible = new_possibilities
        if goal in possible:
            collections += goal
            print("Found ", goal, " in: ", possible)
        else:
            print("NOT Found ", goal, " in: ", possible)
    print(collections)


day = "7"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day7_1(testFile)
# day7_1(realFile)
#
# day7_2(testFile)
day7_2(realFile)
