import numpy as np
from simplex_tools import find_J_not_basis, find_A_not_basis
from simplex_tools import initial_phase as simplex

def check_integer(x):
    for x_i in x:
        if not float(x_i).is_integer():
            return False
    return True


def get_index(x, J_b):
    for index in range(len(J_b)):
        if not x[J_b[index]].is_integer():
            return index


def method_gomori(c, A, b):
    while True:
        m, n = A.shape[0], A.shape[1]
        x, J_b = simplex(A, b)
        x = [round(item, 2) for item in x]
        J_n = find_J_not_basis(np.linspace(0, np.shape(A)[1] - 1, np.shape(A)[1], dtype=int), J_b)
        print('-' * 50)
        print('A: \n' + str(A))
        print('b: ' + str(b))
        print('c: ' + str(c))
        print('x: ' + str(x))
        print('J_b: ' + str(J_b))
        print('J_n: ' + str(J_n))
        if check_integer(x) == True:
            break
        index_k = get_index(x, J_b)
        print('Index: ' + str(index_k))
        A_basis = np.zeros((m, len(J_b)))
        for i in range(len(J_b)):
            A_basis[:, i:i + 1] = A[:, J_b[i]:J_b[i] + 1]
        Ab_inv = np.linalg.inv(A_basis)
        print('Inverse basis matrix:\n' + str(Ab_inv))
        Ab_n = find_A_not_basis(A, J_n)
        print('Not basis matrix:\n' + str(Ab_n))
        matrix_dot = np.dot(Ab_inv, Ab_n)
        print('Multi matrix:\n' + str(matrix_dot))
        new_row = np.zeros(n)
        for i in range(len(J_n)):
            if matrix_dot[index_k][i] >= 0:
                new_row[J_n[i]] = matrix_dot[index_k][i]
            else:
                new_row[J_n[i]] = matrix_dot[index_k][i]
        A_new_temp = np.vstack([A, new_row])

        new_column = [[0] for _ in range(A_new_temp.shape[0] - 1)]
        new_column.append([-1])

        A = np.append(A_new_temp, new_column, axis=1)
        if x[index_k] >= 0:
            b = np.append(b, x[index_k] - int(x[index_k]))
        else:
            b = np.append(b, x[index_k] - int(x[index_k] - 1))
        np.concatenate((c, [0]))
    return x


def test_1():
    A = np.array([[-4, 6, 1, 0], [1, 1, 0, 1]])
    b = np.array([9, 4])
    c = np.array([-1, 2])
    return c, A, b


if __name__ == '__main__':
    c, A, b = test_1()
    print(method_gomori(c, A, b))
