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

print(common((1, 2, 3, 4), [6,4,2]))