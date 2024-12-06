import numpy as np

def day2_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    count_safe = 0
    for line in lines:
        nums = np.asarray([int(x) for x in line.split()])
        diffs = getDiffs(nums)
        if is_safe(diffs):
            count_safe += 1

    print(count_safe)

def getDiffs(list):
    return list[:-1] - list[1:]

def is_safe(test_list):
    maxy = np.max(test_list)
    miny = np.min(test_list)
    return not max(abs(maxy), abs(miny)) > 3 and (maxy * miny) > 0


def day2_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    count_safe = 0
    for line in lines:
        nums = np.asarray([int(x) for x in line.split()])
        diffs = getDiffs(nums)
        print(count_safe, nums)
        print(diffs)
        if is_safe(diffs):
            count_safe += 1
        else:
            count_safe += skip_levels(np.copy(diffs), nums)
            count_safe += skip_levels(np.copy(diffs * (-1)), nums)

    print(count_safe)


def skip_levels(diffs, nums):
    used_skip = False
    i = 0
    while i < len(diffs):
        if diffs[i] not in (1, 2, 3):
            if used_skip:
                return 0
            elif i == 0 or i == len(diffs) -1:
                diffs = np.delete(diffs, i)
            else:
                diffs[i] += diffs[i + 1]
                diffs = np.delete(diffs, i + 1)
            used_skip = True
        else:
            i += 1
    print(diffs)
    return 1


testFile = "InputFiles/day2test1.txt"
realFile = "InputFiles/day2real1.txt"

# day2_1(testFile)
# day2_1(realFile)
# day2_2(testFile)
day2_2(realFile)