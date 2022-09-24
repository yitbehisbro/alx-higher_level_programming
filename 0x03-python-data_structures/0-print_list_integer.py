#!/usr/bin/python3
def print_list_integer(my_list=[]):
    while len(my_list) >= 0:
        print("{}".format(*my_list, sep = "\n"))
