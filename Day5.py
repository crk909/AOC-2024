import numpy as np
from collections import defaultdict


def checkPrint(printList, beforeMap):
    print(printList)
    already_printed = set()
    cannot_print = set()
    for i in printList:
        if i in cannot_print:
            return False
        already_printed.add(i)
        need_before = beforeMap[i]
        for j in need_before:
            if j not in already_printed:
                cannot_print.add(j)

    return True


def day5_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    before = defaultdict(set)
    middles = 0
    rules_done = False
    for line in lines:
        if line.strip() == "":
            rules_done = True
            print(before)
        elif not rules_done:
            x,y = [int(x) for x in line.strip().split('|')]
            before[y].add(x)
        else:
            toPrint = [int(x) for x in line.strip().split(',')]
            if checkPrint(toPrint, before):
                print(toPrint[(len(toPrint)-1)//2])
                middles += toPrint[(len(toPrint)-1)//2]
    print(middles)


def reOrder(toPrint, before):
    unprinted = set(toPrint)
    printed = []

    while len(unprinted) != 0:
        for i in unprinted:
            need_before = before[i]
            if not unprinted & need_before:
                # If any in need_before in unprinted, cannot choose i
                printed.append(i)
                unprinted.remove(i)
                break
    return printed[(len(printed)-1)//2]


def day5_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    before = defaultdict(set)
    middles = 0
    rules_done = False
    for line in lines:
        if line.strip() == "":
            rules_done = True
            print(before)
        elif not rules_done:
            x, y = [int(x) for x in line.strip().split('|')]
            before[y].add(x)
        else:
            toPrint = [int(x) for x in line.strip().split(',')]
            if not checkPrint(toPrint, before):
                #Get real ordering
                middles += reOrder(toPrint, before)
    print(middles)


day = "5"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day5_1(testFile)
# day5_1(realFile)
#
# day5_2(testFile)
day5_2(realFile)
