#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the
response (decoded in utf-8). """
from urllib.error import HTTPError
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as error:
        if error.code:
            print("Error code: {}".format(error.code))
        else:
            print("Index")
