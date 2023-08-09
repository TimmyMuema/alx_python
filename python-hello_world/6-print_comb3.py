#!/usr/bin/python3
def combinations(i, j):
    if i < j:
        return str(i) + str(j)
    else:
        return ''

print(', '.join([combinations(i, j) for i in range(10) for j in range(10)]))

