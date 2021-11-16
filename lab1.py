import numpy as np
import math
from scipy.optimize import linprog as simplex


def get_row(c, i, number):
    row = []
    for index, ind in zip(np.zeros(len(c)), range(len(c))):
        if ind == i:
            index = number
        row.append(index)
    return row


def branch_border_method(c, A, b, bnd):
    x_optimal = []
    record = -np.inf
    stack_ab = list()
    stack_ab.append([A, b])
    while True:

        if len(stack_ab) == 0:
            break

        next_ilp = stack_ab.pop()
        next_A, next_b = next_ilp[0], next_ilp[1]
        res_simplex = simplex(c=c, A_ub=next_A, b_ub=next_b, bounds=bnd, method="simplex")
        vector_x = res_simplex.x

        print(50 * "-")
        print('TASK ILP --> \nA: ' + str(next_A) + '\nb: ' + str(next_b))
        print('Vector x: ' + str(vector_x))

        if not res_simplex.success:
            continue

        x_float, index_x_float = None, None

        for x, index_xi in zip(vector_x, range(len(vector_x))):
            if x.is_integer():
                continue
            x_float = x
            index_x_float = index_xi

        new_record = np.dot(c, vector_x)
        print('Current record: ' + str(new_record))

        if not x_float:
            if new_record > record:
                record = new_record
                x_optimal = vector_x

        if new_record <= record:
            continue

        left_A = next_A.copy()
        left_A.append(get_row(c, index_x_float, -1))
        left_b = next_b.copy()
        left_b.append(math.ceil(x_float))

        right_A = next_A.copy()
        right_b = next_b.copy()
        right_A.append(get_row(c, index_x_float, 1))
        right_b.append(math.floor(x_float))

        stack_ab.append([left_A, left_b])
        stack_ab.append([right_A, right_b])

    return x_optimal


def test_1():
    c = [-1, -1]
    A = [[2, 11],
         [1, 1],
         [4, -5]]
    b = [38, 7, 5]
    bnd = [(0, np.inf),
           (0, np.inf)]
    return c, A, b, bnd


def test_2():
    c = [-7, -9]
    A = [[-1, 3],
         [7, 1]]
    b = [6, 35]
    bnd = [(0, np.inf),
           (0, np.inf)]
    return c, A, b, bnd


def test_3():
    c = [-2, -3]
    A = [[3, 4],
         [2, 5]]
    b = [24, 22]
    bnd = [(0, np.inf),
           (0, np.inf)]
    return c, A, b, bnd


if __name__ == '__main__':
    c, A, b, bnd = test_1()
    print(branch_border_method(c, A, b, bnd))
