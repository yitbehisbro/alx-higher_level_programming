#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        print(" ".join("{:d}".format(matrix[i])))
