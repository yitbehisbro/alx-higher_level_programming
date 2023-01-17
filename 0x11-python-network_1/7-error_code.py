#!/usr/bin/python3
""" Prints the error code value """
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    print(result.content.decode('utf-8'))
