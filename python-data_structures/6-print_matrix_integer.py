#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_string = ""
        for i in range(len(row)):
            if i > 0:
                row_string += " "
            row_string += "{:d}".format(row[i])
        print(row_string)
