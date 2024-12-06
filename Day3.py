import numpy as np
import re

def day3_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    regexFilter = "mul\(\\d+,\\d+\)"
    matches = []
    for line in lines:
        matches.extend(re.findall(regexFilter, line))

    first_nums = np.asarray([int((re.search('\\d+', x)).group()) for x in matches])
    second_nums = np.asarray([int((re.search(',\\d+', x)).group().strip(',')) for x in matches])
    print(first_nums)
    print(second_nums)
    mults = first_nums * second_nums
    print(np.sum(mults))

def day3_2(filename):
    f = open(filename, 'r')
    lines = f.read().replace('\n','')
    regexFilter = "mul\(\\d+,\\d+\)"
    doFilter = "do\(\)"
    dontFilter = "don't\(\)"

    matches = []
    starts = []
    stops = []
    matches.extend(re.finditer(regexFilter, lines))
    starts.extend(re.finditer(doFilter, lines))
    stops.extend(re.finditer(dontFilter, lines))
    print(len(matches))

    first_nums = np.asarray([int((re.search('\\d+', x.group())).group()) for x in matches])
    second_nums = np.asarray([int((re.search(',\\d+', x.group())).group().strip(',')) for x in matches])
    match_locations = [int(x.span()[0]) for x in matches]
    starts = [int(x.span()[0]) for x in starts]
    stops = [int(x.span()[0]) for x in stops]
    starts.append(match_locations[-1] + 1)
    stops.append(match_locations[-1] + 1)
    allow_matches = True

    print(match_locations)
    print(match_locations[-1])
    print(starts)
    print(stops)

    stops_pointer = 0
    starts_pointer = 0
    total_sum = 0
    for i in range(len(match_locations)):
        this_match = match_locations[i]
        while(this_match > min(starts[starts_pointer], stops[stops_pointer])):
            if starts[starts_pointer] < stops[stops_pointer]:
                allow_matches = True
                starts_pointer += 1
            else:
                allow_matches = False
                stops_pointer += 1
        if allow_matches:
            print(this_match)
            total_sum += first_nums[i] * second_nums[i]
    print(total_sum)



day = "3"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day3_1(testFile)
# day3_1(realFile)

# day3_2(testFile)
# day3_2(testFile2)
# day3_2(moreTests)
day3_2(realFile)