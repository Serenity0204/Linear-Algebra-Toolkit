from sympy import Matrix


def find_rref(twoDArr):
    matrix = Matrix(twoDArr)
    rref_matrix, _ = matrix.rref()
    rref_list = rref_matrix.tolist()
    return rref_list


def basis_helper(bases_list):
    basis_str = ""
    count = 0
    for basis in bases_list:
        temp = "<"
        for i in range(0, len(basis)):
            temp += str(basis[i][0])
            if i != (len(basis) - 1):
                temp += ","
        temp += ">"
        basis_str += temp
        if count != (len(bases_list) - 1):
            basis_str += ", "
        count += 1
    if len(basis_str) == 0:
        basis_str += "zero vector"
    return basis_str


def find_nullspace(twoDArr):
    matrix = Matrix(twoDArr)
    rref_matrix, _ = matrix.rref()
    nullspace_basis = rref_matrix.nullspace()
    bases_list = []
    for basis in nullspace_basis:
        basis_vector = basis.tolist()
        bases_list.append(basis_vector)
    nullspace_str = "Ker(Input Matrix) = Nullspace(Input Matrix) = Span({"

    nullspace_str += basis_helper(bases_list)
    nullspace_str += "})"
    return nullspace_str


def find_colspace(twoDArr):
    matrix = Matrix(twoDArr)
    colspace_basis = matrix.columnspace()
    bases_list = []
    for basis in colspace_basis:
        basis_vector = basis.tolist()
        bases_list.append(basis_vector)
    colspace_str = "Range(Input Matrix) = Colspace(Input Matrix) = Span({"
    colspace_str += basis_helper(bases_list)
    colspace_str += "})"
    return colspace_str


def find_rowspace(twoDArr):
    matrix = Matrix(twoDArr)
    row_basis = matrix.rowspace()
    bases_list = []
    for basis in row_basis:
        basis_vector = basis.tolist()
        bases_list.append(basis_vector)
    rowspace_str = "Rowspace(Input Matrix) = Span({"
    rowspace_str += basis_helper(bases_list)
    rowspace_str += "})"
    return rowspace_str


# def find_eigenspace(twoDArr):
#     matrix = Matrix(twoDArr)
#     eigen_basis = matrix.eigenvects()
