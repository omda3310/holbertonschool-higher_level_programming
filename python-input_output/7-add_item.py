#!/usr/bin/python3
"""add_item method"""


import sys
import os.path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []
    """Extend the list"""
    my_list.extend(sys.argv[1:])
    """Save the list"""
    save_to_json_file(my_list, "add_item.json")
