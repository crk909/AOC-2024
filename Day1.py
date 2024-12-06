import numpy as np

def day1_1(filename):
    f = open(filename, 'r')
    first = []
    second = []
    lines = f.readlines()
    for line in lines:
        spline = line.split(" ")
        first.append(int(spline[0]))
        second.append(int(spline[-1]))
    first = np.asarray(sorted(first))
    second = np.asarray(sorted(second))

    results = abs(first - second)
    # print(first)
    # print(second)
    # print(results)
    print(np.sum(results))

def day1_2(filename):
    f = open(filename, 'r')
    first = []
    dicto = {}
    lines = f.readlines()
    for line in lines:
        spline = line.split(" ")
        first.append(int(spline[0]))
        second = int(spline[-1])
        dicto[second] = dicto.get(second, 0) + 1


    similarities = [i * dicto.get(i, 0) for i in first]
    # print(similarities)
    print(sum(similarities))


testFile = "InputFiles/day1test1.txt"
realFile = "InputFiles/day1real1.txt"

# day1_1(testFile)
# day1_1(realFile)
# day1_2(testFile)
day1_2(realFile)