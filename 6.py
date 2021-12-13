import numpy as np


def task_6(D_start, R_start):
    D = D_start
    for k in range(D_start.shape[0]):
        D_next = np.zeros(shape=D_start.shape)
        R_next = np.zeros(shape=D_start.shape)
        for i in range(D_start.shape[0]):
            for j in range(D_start.shape[0]):
                D_next[i][j] = np.min([D[i][j], D[i][k] + D[k][j]])
                if D_next[i][j] == D[i][j]:
                    R_next[i][j] = R_start[i][j]
                else:
                    R_next[i][j] = R_start[i][k]
        D = D_next
        R_start = R_next
    return D, R_start


if __name__ == '__main__':

    D_start = np.array(
    [
        [0, 9, np.inf, 3,  np.inf,  np.inf,  np.inf,  np.inf],
        [9, 0, 2, np.inf, 7, np.inf,  np.inf,  np.inf],
        [np.inf, 2, 0, 2, 4, 8, 6, np.inf],
        [3,  np.inf, 2, 0, np.inf,  np.inf, 5, np.inf],
        [np.inf, 7, 4,  np.inf, 0, 10, np.inf,np.inf],
        [np.inf, np.inf, 8,  np.inf, 10, 0, 7,  np.inf],
        [ np.inf, np.inf, 6, 5,  np.inf, 7, 0,  np.inf],
        [ np.inf,  np.inf,  np.inf,  np.inf, 9, 12, 10, 0]])
    R_start = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
   ])
    D, R = task_6(D_start, R_start)
    print(D)
    print('\n')
    print(R)
