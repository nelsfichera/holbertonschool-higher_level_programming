#!/usr/bin/python3
'''divides a matrix by given num'''


def matrix_divided(matrix, div):
    ''' matrix_divided: divides each element in a matrix
    by given number. accepted args are matrix (list),
    and div (int, float). returns the matrix reloaded, aka
    a matrix in which each element is the quotient of
    the original matrix and the given number rounded to 2 decimal places.
    this function raises errors when incorrect types
    are used and when the user attempts to divide
    by zero.
    '''

    '''Error messages'''
    matrixType_error = "matrix must be a matrix (list of lists) of integers/floats"
    matrixSize_error = "Each row of the matrix must have the same size"
    divType_error = 'div must be a number'
    divZero_error = 'division by zero'

    '''init resulting matrix'''
    quotient_matrix = []

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(matrixType_error)
    if type(div) not in (int, float):
        raise TypeError(divType_error)
    if div == 0:
        raise ZeroDivisionError(divZero_error)

    for row in matrix:
        quotient_row = []
        if type(row) is not list or len(row) == 0:
            raise TypeError(matrixType_error)
        elif len(row) != len(matrix[0]):
            raise TypeError(matrixSize_error)

        for element in row:
            if type(element) not in (int, float):
                raise TypeError(matrixType_error)
            quotient_row.append(round((element / div), 2))
        quotient_matrix.append(quotient_row)
    return (quotient_matrix)
