#!/usr/bin/python3
""" Pascal's Triangle module"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    lists = []
    tmp = []
    for i in range(n):
        result = []
        a, b = -1, 0
        for j in range(len(tmp) + 1):
            if a == -1 or b == len(tmp):
                result += [1]
            else:
                result += [tmp[a] + tmp[b]]
            a += 1
            b += 1
        lists.append(result)
        tmp = result[:]
    return lists
