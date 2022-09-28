#!/usr/bin/python3
def weight_average(my_list=[]):
    n, d = 0, 0
    if not my_list:
        return 0
    else:
        for t in my_list:
            n += t[0] * t[1]
            d += t[1]
        return n / d
