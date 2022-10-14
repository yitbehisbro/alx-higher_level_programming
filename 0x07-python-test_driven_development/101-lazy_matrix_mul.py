#!/usr/bin/python3
""" Lazy matrix multiplication """


import numpy as n
def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices by using the module NumPy """
    mul = n.dot(m_a, m_b)
    return mul
