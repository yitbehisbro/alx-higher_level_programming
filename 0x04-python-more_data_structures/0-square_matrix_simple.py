#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for x in range(0, len(matrix)):
            square = list(map(lambda i: pow(i, 2), matrix[x]))
            new_matrix.append(square)
        return new_matrix
