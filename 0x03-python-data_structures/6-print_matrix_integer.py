#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m_list in matrix:
        print(" ".join("{:d}".format(elements) for elements in m_list))
