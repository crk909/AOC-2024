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
        if is_safe(diffs):
            count_safe += 1
        else:
            pos = skip_levels(np.copy(diffs), nums)
            neg = skip_levels(np.copy(diffs * (-1)), nums)
            if pos or neg:
                count_safe += 1


    print(count_safe)


def skip_levels(indiffs, nums):
    for i in range(len(indiffs)):
        if indiffs[i] not in (1, 2, 3):
            if i == 0:
                # print("First element")
                delFirst = np.delete(indiffs, i)
                delSecond = np.copy(indiffs[1:])
                delSecond[0] += indiffs[0]
                return is_safe(delFirst) or is_safe(delSecond)
            elif i == len(indiffs) - 1:
                # print("Last element")
                return True
            else:
                # print("Tried con 3 on pos:", i)
                delHere = np.copy(indiffs[i + 1:])
                delHere[0] += indiffs[i]
                delHere = np.append(delHere, indiffs[0])

                delPrev = np.copy(indiffs[i:])
                delPrev[0] += indiffs[i - 1]
                delPrev = np.append(delPrev, indiffs[0])
                # print(delPrev, delHere)
                return is_safe(delHere) or is_safe(delPrev)

    print("This is bad...")
    return False


testFile = "InputFiles/day2test.txt"
realFile = "InputFiles/day2real.txt"
moreTests = "InputFiles/day2moretests.txt"

# day2_1(testFile)
# day2_1(realFile)
# day2_2(testFile)
# day2_2(moreTests)
day2_2(realFile)
