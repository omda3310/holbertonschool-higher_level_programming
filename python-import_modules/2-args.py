#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)
if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}: ".format(num_args, "" if num_args == 1 else "s"), end="")
    print(*args, sep=", ")
for i in range(num_args):
    print("{}: {}".format(i+1, args[i]))
