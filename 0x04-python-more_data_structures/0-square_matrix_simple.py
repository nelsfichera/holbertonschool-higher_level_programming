#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = 0
    matrix_reloaded = matrix.copy()
    while x < len(matrix):
        matrix_reloaded[x] = list(map(lambda n: n * n, matrix[x]))
        x += 1
    return(matrix_reloaded)
