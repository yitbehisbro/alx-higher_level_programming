#!/usr/bin/python3
def magic_calculation(a, b):
    magic = 0
    for j in range(1, 3):
        try:
            if (j > a):
                raise Exception("Too far")
            else:
                magic += (a ** b) / j
        except (TypeError, ValueError, ZeroDivisionError, NameError, RuntimeError):
            magic = b + a
            break
    return magic
