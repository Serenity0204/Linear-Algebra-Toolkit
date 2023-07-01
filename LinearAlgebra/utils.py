from sympy import Matrix


def find_rref(twoDArr):
    matrix = Matrix(twoDArr)
    rref_matrix, _ = matrix.rref()
    rref_list = rref_matrix.tolist()
    return rref_list


