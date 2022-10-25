#!/usr/bin/python3
""" Load, add, save file module"""
import os.path as path
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

obj = []
if path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
for i in sys.argv[1:]:
    obj.append(i)
save_to_json_file(obj, "add_item.json")
