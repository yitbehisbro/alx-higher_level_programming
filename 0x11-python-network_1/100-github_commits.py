#!/usr/bin/python3
""" Lists 10 commits (from the most recent to oldest) of the
repository rails by the user rails
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    try:
        result = requests.get(url)

        if result.status_code == 200:
            r = result.json()
            for i in range(0, 10):
                print("{}: {}".format(
                    r[i].get('sha'),
                    r[i].get('commit').get('author').get('name')
                    ))
    except Exception:
        pass
