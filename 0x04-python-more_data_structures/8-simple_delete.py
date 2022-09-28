#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None and key is not None:
        if a_dictionary.get(key) is not None:
            del a_dictionary[key]
            return a_dictionary
        else:
            return a_dictionary
