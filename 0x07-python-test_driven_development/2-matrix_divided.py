#!/usr/bin/python3
"""defines a function to divide a matrix by a scalar."""


def matrix_divided(matrix, div):
    """divides a matrix by a scalar integer, rounding the result to two decimal places."""
    import decimal
    
    # Define an error message for type checking
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if 'matrix' is a list
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
        
         # Check if all rows have the same length
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
        
        # Check if 'div' is a number
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
