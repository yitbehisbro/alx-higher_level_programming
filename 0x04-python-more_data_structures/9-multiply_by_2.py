#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        for i in list(a_dictionary):
            print("{}: {}".format(i, a_dictionary.get(i) * 2))
