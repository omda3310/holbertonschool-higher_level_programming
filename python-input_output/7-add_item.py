#!/usr/bin/python3
"""add all arguments and save them to a file"""
import sys
import os.path
from json import load, dump


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
fl = "add_item.json"
arg = sys.argv[1:]
mlist = []

if os.path.exists(fl):
    mlist = load_from_json_file(fl)

for i in range(1, len(arg)):
    mlist.append(arg[i])

save_to_json_file(mlist, fl)
