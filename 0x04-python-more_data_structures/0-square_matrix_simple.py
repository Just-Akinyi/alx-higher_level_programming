#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrx = ([[c**2 for c in row] for row in matrix])
    return(new_matrx)
