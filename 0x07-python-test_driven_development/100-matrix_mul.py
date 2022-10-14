#!/usr/bin/python3
""" Matrix multiplication """


def matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices:
        Args:
            m_a (list): first matrix
            m_b (list): second matrix
        Returns: matrix multplication
        Raises:
            TypeError: if m_a and m_b are not a list or equal
            ValueError: if m_a and m_b can’t be multiplied or empty
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    m1 = len(m_a)
    if m1 == 0:
        raise ValueError("m_a can't be empty")
    m2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if m2 is None:
            m2 = len(i)
            if m2 == 0:
                raise ValueError("m_a can't be empty")
        if m2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    m3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if m3 is None:
            m3 = len(i)
            if m3 == 0:
                raise ValueError("m_b can't be empty")
        if m3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if m2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = []
    last = []
    for i in range(m1):
        for j in range(m2):
            n = 0
            for k in range(m2):
                n += m_a[i][k] * m_b[k][j]
            last.append(n)
        product.append(last)
    return product
