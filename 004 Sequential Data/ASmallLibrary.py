import numpy as np

def filter(seq, ignore):
    ret = []
    for value in seq:
        if value not in ignore:
            ret.append(value)
    return ret


def find(seq, val):
    indizies = []
    for i in range(len(seq)):
        if(seq[i] == val):
            indizies.append(i)
    return indizies


def common(seq1, seq2):
    doubles = []
    for value1 in seq1:
        for value2 in seq2:
            if(value1 == value2 and value1 not in doubles):
                doubles.append(value1)
    return doubles

print(filter(np.array([1, 10, 4, 6, 10, 10, 9, 3, 2, 6, 9]), [6]))
print(find((6, 10, 2, 7, 7, 4, 5, 2, 7, 3, 3), 6))
print(find([9.8, 1.4, 5.1, 2.2, 2.9, 9.8, 4.6, 9.9, 9.9, 2.1], 9.9))
print(common([6, 10, 2, 7, 7, 4, 5, 2, 7, 3, 3], [1, 10, 4, 6, 10, 10, 9, 3, 2, 6, 9]))


list1 = [27, 99, 49, 47, 68, 41, ' ', 34, 33, 42, ' ', 74, 53, 52, 25, 46, 84, 48, ' ', 37, 50, 71, 60]
list2 = [' ', 60, 66, 83, 47, 39, 51, 25, 76, 44, ' ', 77, 73, 12, 75, 96, 55, 84, 54, 29, ' ', 11, 52]
common_list = common(filter(list1, [' ']), filter(list2, [' ']))
largest = max(common_list)
print(find(list1, largest), find(list2, largest))