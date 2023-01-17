#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests
import sys


if __name__ == "__main__":
    param = {'q': ''}

    try:
        if sys.argv[1]:
            param['q'] = sys.argv[1]
    except Exception:
        pass

    try:
        result = requests.post("http://0.0.0.0:5000/search_user", data=param)
        my_json = result.json()
        if my_json:
            print("[{}] {}".format(my_json.get('id'), my_json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
