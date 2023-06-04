#!/usr/bin/python
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    summ = sum(int(arg) for arg in args)
    print(summ)
