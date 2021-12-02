def resource_allocation_task(x, f, n, c):
    B = list([])
    x_0 = [[f[0][i] for i in range(len(x))]]
    B.append([0 for i in range(len(x))])
    for i in range(len(x)):
        B[0][i] = f[0][i]
    for i in range(1, n):
        arr = []
        arr_for_x_0 = []
        for xi in x:
            list_bk = [0 for _ in range(len(x))]
            for j, _x in enumerate(x):
                if (xi - _x) >= 0:
                    p = x.index(xi-_x)
                    list_bk[j] = f[i][j] + B[-1][p]
            b_k = max(list_bk)
            arr.append(b_k)
            arr_for_x_0.append(list_bk.index(b_k))
        B.append(arr)
        x_0.append(arr_for_x_0)
    print("B: ")
    for i in B:
        print(i)
    print("x_o: ")
    for i in x_0:
        print(i)
    vector_x = list()
    for i in reversed(range(len(B))):
        J = x_0[i][x.index(c)]
        c = c - x[J]
        vector_x.append(x[J])
    print('Оптимальный план:' + str(vector_x))
    return vector_x


if __name__ == '__main__':
    X = [0, 1, 2, 3, 4, 5]
    F = [[0, 1, 2, 3, 4, 5],
         [0, 0, 1, 2, 4, 7],
         [0, 2, 2, 3, 3, 5]]
    N = 3  # K
    C = 5  # y
    H = resource_allocation_task(X, F, N, C)
