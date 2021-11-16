import numpy as np
import copy
import math


# lab 1
def find_invertible_matrix(A, l, i, optimization=False):
    n = len(A[i])
    l_temp = copy.copy(l)
    l_temp[i] = -1
    L = (-1 / l[i]) * l_temp
    E = np.eye(n)
    E[:, i:i + 1] = L
    result = np.zeros((n, n))
    if optimization:
        for k in range(n):
            for j in range(n):
                result[k][j] = E[k][i] * A[i][j]
                if k != i:
                    result[k][j] += E[k][k] * A[k][j]
    else:
        result = E.dot(A)
    return result


def is_matrix_invertible(A, x):
    return A.dot(x)


def find_A_not_basis(A, J_not_b):
    m = np.shape(A)[0]
    n = len(J_not_b)
    A_not_basis = np.zeros((m, n))
    for i in range(n):
        A_not_basis[:, i:i + 1] = A[:, J_not_b[i]:J_not_b[i] + 1]
    return A_not_basis


def invert_matrix(A, x, i):
    l = is_matrix_invertible(A, x)
    if l[i]:
        return find_invertible_matrix(A, l, i, optimization=True)
    else:
        print('Matrix is not invertible')
        return None


# lab 2
def create_A_basis_inv(A_prev, A, J_basis, i):
    m = np.shape(A)[0]
    n = len(J_basis)
    if i is not None:
        # lab1 func
        A_basis_inv = invert_matrix(A_prev, A[:, J_basis[i]:J_basis[i] + 1], i)
    else:
        A_basis = np.zeros((m, n))
        for i in range(n):
            A_basis[:, i:i + 1] = A[:, J_basis[i]:J_basis[i] + 1]
        A_basis_inv = np.linalg.inv(A_basis)
    return A_basis_inv


def find_J_not_basis(J, J_basis):
    J_not_basis = []
    for i in range(len(J)):
        if J[i] not in J_basis:
            J_not_basis.append(J[i])
    return J_not_basis


def find_theta_0(x, z, J_basis):
    thetas = []
    for i in range(len(z)):
        if z[i][0] <= 0:
            thetas.append(math.inf)
        else:
            thetas.append(x[J_basis[i]] / z[i][0])
    theta_0 = min(thetas)
    index = thetas.index(theta_0)
    return theta_0, index


def new_x(x, J_basis, j_0, theta_0, z):
    for j in range(len(x)):
        if j not in J_basis:
            x[j] = 0
        elif j == j_0:
            x[j] = theta_0
    for i in range(len(J_basis)):
        if J_basis[i] == j_0:
            continue
        x[J_basis[i]] -= theta_0 * z[i][0]
    return x


def find_c_basis(c, m, J_basis):
    c_basis = np.zeros(m)
    for i in range(m):
        c_basis[i] = c[J_basis[i]]
    return c_basis


def main_phase(c, A, x, J_basis):
    J = np.linspace(0, np.shape(A)[1] - 1, np.shape(A)[1], dtype=int)
    m = np.shape(A)[0]
    j_i, A_basis_inv = None, None
    while True:
        j_0 = None
        A_basis_inv = create_A_basis_inv(A_basis_inv, A, J_basis, j_i)
        c_basis = find_c_basis(c, m, J_basis)
        u = c_basis.dot(A_basis_inv)
        delta = u.dot(A) - c
        J_not_basis = find_J_not_basis(J, J_basis)
        for i in range(len(J_not_basis)):
            if delta[J_not_basis[i]] < 0:
                j_0 = J_not_basis[i]
                break
        if j_0 is None:
            return x, J_basis
        z = A_basis_inv.dot(A[:, j_0: j_0 + 1])
        theta_0, j_i = find_theta_0(x, z, J_basis)
        if theta_0 == math.inf:
            return 'There is no optimal plan for such combination'
        J_basis[j_i] = j_0
        x = new_x(x, J_basis, j_0, theta_0, z)


# lab 3
def initial_phase(A, b):
    for i in range(len(b)):
        if b[i] < 0:
            b[i] *= (-1)
            A[i, :] *= (-1)
    (m, n) = np.shape(A)
    c_new = np.zeros(n + m)
    for i in range(m):
        c_new[n + i] = -1
    A_new = np.zeros((m, m + n))
    E = np.eye(m)
    for i in range(m):
        A_new[i] = np.concatenate((A[i], E[i]))
    x_new = []
    for i in range(n + m):
        x_new.append(0)
    for i in range(m):
        x_new[n + i] = b[i]
    J_b = [i for i in range(n, n + m)]
    x_opt, J_opt = main_phase(c_new, A_new, x_new, J_b)
    if x_opt is None or J_opt is None:
        return
    for i in range(n, n + m):
        if x_opt[i] != 0:
            print('This task is incompatible')
            return None, None
    x_answ = list(x_opt[i] for i in range(n))
    for i in range(len(J_opt)):
        l = []
        j_k, k, index = 0, 0, 0
        if J_opt[i] >= n:
            j_k = J_opt[i]
            index = J_opt[i] - n
            k = i
            J = [t for t in range(n + m)]
            J_not_b = find_J_not_basis(J, J_opt)
            J_not_b = list(J_not_b[i] for p in range(len(J_not_b)) if J_not_b[p] < n)
            A_b = np.zeros((m, len(J_opt)))
            for z in range(len(J_opt)):
                A_b[:, z:z + 1] = A_new[:, J_opt[z]:J_opt[z] + 1]
            A_b_inv = np.linalg.inv(A_b)
            for z in range(len(J_not_b)):
                l.append(np.around(A_b_inv.dot(A_new[:, J_not_b[z]:J_not_b[z] + 1]), decimals=5))
            case_2 = True
            for z in range(len(l)):
                if l[z][k] != 0:
                    case_2 = False
                    J_opt[J_opt.index(j_k)] = J_not_b[z]
            if case_2:
                A[index] = np.zeros(n)
                A_new[index] = np.zeros(n + m)
                c_new[j_k] = 0
                J_opt.remove(j_k)
    return x_answ, J_opt