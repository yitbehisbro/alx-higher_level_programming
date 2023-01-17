#!/usr/bin/python3
""" Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    result = requests.get("https://api.github.com/user", auth=(usr, pwd))
    if result.status_code == 200:
        result = result.json()
        print("{}".format(result["id"]))
    else:
        print("None")
