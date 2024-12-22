import numpy as np


def in_range(current_pos, lowBound, upperBound):
    return lowBound <= current_pos[0] <= upperBound and lowBound <= current_pos[1] <= upperBound


def move(direction, current_pos):
    match direction:
        case 'U':
            return current_pos[0] - 1, current_pos[1]
        case 'D':
            return current_pos[0] + 1, current_pos[1]
        case 'L':
            return current_pos[0], current_pos[1] - 1
        case 'R':
            return current_pos[0], current_pos[1] + 1


def day6_1(filename):
    f = open(filename, 'r')
    spools = set()
    visited = set()
    current_pos = (0,0)
    direction = 'U'
    turns = {'U':'R',
             'R':'D',
             'D':'L',
             'L':'U'}
    # Set of spool locations
    lines = f.readlines()
    size = len(lines)
    for i, line in enumerate(lines):
        nump = np.asarray(list(line.strip()))
        # print(i, nump)
        for x in np.where(nump=='#')[0]:
            spools.add((i,x))
        for y in np.where(nump=='^')[0]:
            current_pos = (i,y)
    # print(spools)
    # print(current_pos)
    while True:
        if not in_range(current_pos, 0, size-1):
            print(current_pos)
            print(len(visited))
            return
        visited.add(current_pos)
        next_location = move(direction, current_pos)
        if next_location not in spools:
            current_pos = next_location
        else:
            direction = turns[direction]


def printLoop(spools_cop, visited, size):
    for i in range(size):
        string = ""
        for j in range (size):
            pos = (i,j)
            if pos in spools_cop:
                string += "# "
            elif pos in visited['U']:
                string += "^ "
            elif pos in visited['D']:
                string += "v "
            elif pos in visited['L']:
                string += "< "
            elif pos in visited['R']:
                string += "> "
            else:
                string += ". "
        print(string)


def tryLooping(current_pos, spools_cop, row, col, size):
    spools_cop.add((row,col))
    turns = dict(U='R', R='D', D='L', L='U')
    visited = dict(U=set(), R=set(), D=set(), L=set())
    direction = "U"

    while in_range(current_pos, 0, size - 1):
        # Add to specified dictionary
        # If already in turned dictionary, adding obstacle would allow it to loop
        next_location = move(direction, current_pos)
        if current_pos in visited[direction]:
            # printLoop(spools_cop, visited, size)
            print(row, col)
            return True
        visited[direction].add(current_pos)
        if next_location not in spools_cop:
            current_pos = next_location
        else:
            direction = turns[direction]
    return False

def day6_2(filename):
    f = open(filename, 'r')
    spools = set()
    start_pos = (0, 0)
    found_obbies = set()
    # Set of spool locations
    lines = f.readlines()
    size = len(lines)
    for i, line in enumerate(lines):
        nump = np.asarray(list(line.strip()))
        for x in np.where(nump == '#')[0]:
            spools.add((i, x))
        for y in np.where(nump == '^')[0]:
            start_pos = (i, y)

    for row in range(size):
        for col in range(size):
            current_pos = start_pos
            if (row,col) != current_pos:
                #doSimulation
                if tryLooping(current_pos, spools.copy(), row, col, size):
                    found_obbies.add((row,col))
    print(found_obbies)
    print(len(found_obbies))


day = "6"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day6_1(testFile)
# day6_1(realFile)
#
# day6_2(testFile)
day6_2(realFile)
