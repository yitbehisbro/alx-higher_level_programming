#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        for i in reversed(range(len(my_list))):
            print("{:d}".format(my_list[i]))
