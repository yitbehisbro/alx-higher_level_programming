#!/usr/bin/python3
""" Divide a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix.
        Args:
            matrix (list): the matrix
            div (int): integer value
        Returns: the qutient of matrix
        Raises:
            TypeError: Each row of the matrix
                must have the same size
            TypeError: div must be a number
            ZeroDivisionError: division by zero
            TypeError: matrix must be a matrix
                (list of lists) of integers/floats
    """
    flag = None
    n = []
    m_copy = matrix.copy()
    message = "Each row of the matrix must have the same size"
    message2 = "matrix must be a matrix (list of lists) of integers/floats"

    if len(m_copy[0]) != len(m_copy[1]):
        raise TypeError(message)
    for row in m_copy:
        for col in range(len(row)):
            if type(row[col]) not in [int, float]:
                flag = 1
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if flag == 1:
        raise TypeError(message2)
    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return n
