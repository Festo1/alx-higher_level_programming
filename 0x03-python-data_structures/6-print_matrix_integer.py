#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        print(" ".join("{:d}".format(x) for x in y))
