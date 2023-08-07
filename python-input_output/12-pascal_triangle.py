#!/usr/bin/python3
"""a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Return list of integer  representing the Pascal’s triangle"""
    if n <= 0:
        return []

    triangle = [1]
    for c in range(1, n):
        c_row = [1]
        p_row = triangle[c - 1]
        for i in range(1, c):
            c_row.append(p_row[i - 1] + p_row[i])
        c_row.append(1)
        triangle.append(c_row)
    return triangle
