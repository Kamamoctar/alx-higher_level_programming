#!/usr/bin/python3
def squar_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), elm)) for elm in matrix]
