#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out_mat = list(map(lambda List: list(map(lambda x: x**2, List)), matrix))
    return out_mat
