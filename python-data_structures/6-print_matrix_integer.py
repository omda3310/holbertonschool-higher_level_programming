#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if row.index(i) != 0:
                print("", end="")
            print("{:d}".format(i), end="")
        print()
