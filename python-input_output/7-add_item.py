#!/usr/bin/python3
"""add all arguments and save them to a file"""
import sys
from os.path import exists
from json import load, dump

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fl = "add_item.json"
arg = sys.argv[1:]

if exists(fl):
    mlist = load_from_json_file(fl)
else:
    mlist = []

mlist.extend(arg)
save_to_json_file(mlist, fl)
