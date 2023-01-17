#!/usr/bin/python3
""" Displays the value of the X-Request-Id variable
found in the header of the response. """
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print("{}".format(response.getheader('X-Request-Id')))
