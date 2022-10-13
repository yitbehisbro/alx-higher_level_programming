#!/usr/bin/python3
""" Print square """


def print_square(size):
    """ Prints a square with the character #. """

    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print(end="\n")
