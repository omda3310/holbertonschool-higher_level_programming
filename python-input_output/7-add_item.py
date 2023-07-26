#!/usr/bin/python3
"""add_item method"""


import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    if os.path.exists("add_item.json"):
        mlist = load_from_json_file("add_item.json")
    else:
        mlist = []
    """Extend the list"""
    mlist.extend(sys.argv[1:])
    """Save the list"""
    save_to_json_file(mlist, "add_item.json")
