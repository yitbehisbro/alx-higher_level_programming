#!/usr/bin/python3
""" Prints the response header value """
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    print(result.headers.get('X-Request-Id'))
