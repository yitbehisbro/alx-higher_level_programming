#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        for i in list(a_dictionary.copy()).keys():
            a_dictionary.copy()[i] *= 2
        return a_dictionary.copy()
