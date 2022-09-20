#!/usr/bin/python3
for i in reversed(range(97, 123)): # Reverses the range
    print("{:c}".format(i if (i % 2 == 0) else (i - 32)), end="")
