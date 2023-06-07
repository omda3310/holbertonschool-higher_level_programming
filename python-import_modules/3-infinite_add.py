#!/usr/bin/python3
import sys
if __name__ == "__main__":
    res = 0
    for i in sys.argv:
        res += int(i)
    print(res)
