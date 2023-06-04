#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    c = len(argv) - 1
    print("{} argument{}.".format(c, "" if c == 1 else "s"), end="")
    print("{}".format("." if c == 0 else ":"))
    if c > 1:
        for i in range(1, c + 1):
            print("{:d}: {}".format(i, argv[i]))
