#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            counter += 1

    print()
    return counter
