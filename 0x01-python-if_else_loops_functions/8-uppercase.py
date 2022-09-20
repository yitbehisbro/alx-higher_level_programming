#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) - 32 if i.islower() else ord(i) - 0), end="")
    print(end="\n")
