#!/usr/bin/python3
"""add all arguments and save them to a file"""
import sys
from os.path import exists
from json import dump, load
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fl = "add_item.json"
if __name__ == "__main__":

    if exists(fl):
        mlist = load_from_json_file(fl)
    else:
        mlist = []

    mlist.extend(sys.argv[1:])
    save_to_json_file(mlist, fl)
