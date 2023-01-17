#!/usr/bin/python3
""" Fetches the URL with requests """
import requests


if __name__ == "__main__":
    page = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(page.content.decode('utf-8'))))
    print("\t- content: {}".format(page.content.decode('utf-8')))
