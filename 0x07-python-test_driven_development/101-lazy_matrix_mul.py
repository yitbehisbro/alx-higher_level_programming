#!/usr/bin/python3
""" Lazy matrix multiplication """


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices by using the module NumPy
        Args:
            m_a (list): first matrix
            m_b (list): second matrix
        Returns: matrix multplication
        Raises:
            TypeError: if m_a and m_b are not a list or equal
            ValueError: if m_a and m_b can’t be multiplied or empty
    """
    return numpy.matmul(m_a, m_b)
