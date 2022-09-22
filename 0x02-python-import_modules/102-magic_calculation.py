#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        r = add(a, b)
        for i in range(4, 6):
            r = add(r, i)
        return r
    else:
        return sub(a, b)
