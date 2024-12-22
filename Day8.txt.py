import numpy as np
from collections import defaultdict
from math import gcd

def in_bounds(position, max_size):
    return 0 <= position[0] <= max_size and 0 <= position[1] <= max_size

def day8_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    antennas = defaultdict(list)
    row = 0
    for line in lines:
        points = list(line.strip())
        for i, freq in enumerate(points):
            if freq != '.':
                antennas[freq].append((row, i))

        row += 1
    size = row - 1
    anodes = set()
    for k in antennas.keys():
        # For each antennaType, make all possible pairs
        antennaType = antennas[k]
        for i, firstAnt in enumerate(antennaType):
            for secondAnt in antennaType[i + 1:]:
                print(firstAnt, "  :  ", secondAnt)
                # Now place Anodes
                diff_row = firstAnt[0] - secondAnt[0]
                diff_col = firstAnt[1] - secondAnt[1]
                # Between: Must have differences in x and y both be divisible by 3, or it is impossible
                # Only one spot on either side
                above = (firstAnt[0] + diff_row, firstAnt[1] + diff_col)
                below = (secondAnt[0] - diff_row, secondAnt[1] - diff_col)
                if in_bounds(above, size):
                    anodes.add(above)
                if in_bounds(below, size):
                    anodes.add(below)
                if abs(diff_row) % 3 == 0 and abs(diff_col) % 3 == 0:
                    # Exactly 2 can be placed between
                    lefty = (firstAnt[0] + (diff_row // 3), firstAnt[1] + (diff_col // 3))
                    righty = (firstAnt[0] + (2 * diff_row // 3), firstAnt[1] + (2 * diff_col // 3))
                    anodes.add(lefty)
                    anodes.add(righty)
                    print(lefty, righty)

        print(len(anodes))

def make_move(position, step):
    return position[0] + step[0], position[1] + step[1]

def day8_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    antennas = defaultdict(list)
    row = 0
    for line in lines:
        points = list(line.strip())
        for i, freq in enumerate(points):
            if freq != '.':
                antennas[freq].append((row, i))

        row += 1
    size = row - 1
    anodes = set()
    for k in antennas.keys():
        # For each antennaType, make all possible pairs
        antennaType = antennas[k]
        for i, firstAnt in enumerate(antennaType):
            for secondAnt in antennaType[i + 1:]:
                # Determine minimum step size
                print(firstAnt, "  :  ", secondAnt)
                # Now place Anodes
                diff_row = firstAnt[0] - secondAnt[0]
                diff_col = firstAnt[1] - secondAnt[1]
                while gcd(diff_col, diff_row) != 1:
                    diff_row = diff_row // gcd(diff_col, diff_row)
                    diff_col = diff_col // gcd(diff_col, diff_row)
                step = (diff_row, diff_col)
                neg_step = (-diff_row, -diff_col)
                # Positive Steps
                current_position = firstAnt
                while in_bounds(current_position, size):
                    anodes.add(current_position)
                    current_position = make_move(current_position, step)
                # Negative Steps
                current_position = firstAnt
                while in_bounds(current_position, size):
                    anodes.add(current_position)
                    current_position = make_move(current_position, neg_step)
    print(len(anodes))


day = "8"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day8_1(testFile)
# day8_1(realFile)
#
# day8_2(testFile)
day8_2(realFile)
