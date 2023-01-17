#!/usr/bin/python3
""" POST an email with the 'requests' """
import requests
import sys


if __name__ == "__main__":
    result = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(result.content)
