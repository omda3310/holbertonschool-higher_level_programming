#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    c = len(argv) - 1
    print("{:d} argument{}".format(c, "" if c == 1 else "s"), end="")
    print("{}".format("." if c == 0 else ":"))
    if c > 0:
        for i in range(1, c + 1):
            print("{:d}: {}".format(i, argv[i]))
