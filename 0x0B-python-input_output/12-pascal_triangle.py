#!/usr/bin/python3
'''pascal's triangle'''


def pascal_triangle(n):
    '''returns list of ints'''
    if n <= 0:
        return []
    pascal = []
    for x in range(0, n):
        row = [1] * (x + 1)
        if x >= 2:
            for i in range(1, x):
                row[i] = prev[i - 1] + prev[i]
                row[-i-1] = row[i]
        prev = row
        pascal.append(row)
    return pascal
