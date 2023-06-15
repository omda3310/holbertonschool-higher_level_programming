#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cp = 0
    for indx in range(0, x):
        try:
            print("{:d}".format(my_list[indx]), end='')
            cp += 1
        except (TypeError, ValueError):
            pass
        print()
        return cp
