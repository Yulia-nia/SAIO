import numpy as np


def dijkstra(matrix, weights, s, t):
    list_v_u = dict((i, np.inf) for i in range(1, len(matrix) + 1))
    list_v_u[s] = 0
    f = dict([(s, 0)])
    all_v = [i + 1 for i in range(len(matrix))]
    current_v = s
    while len(all_v):
        neighbors = matrix[current_v]
        for neighbor in neighbors:
            neighbor_sum = list_v_u[current_v] + weights[(current_v, neighbor)]
            if neighbor_sum < list_v_u[neighbor]:
                list_v_u[neighbor] = neighbor_sum
                f[neighbor] = current_v
        all_v.remove(current_v)
        current_v = min(list_v_u.items(), key=lambda x: x[1] if x[0] in all_v else np.inf)[0]
    return f


def print_min_way(way, t, s):
    res = []
    v = t
    while True:
        res.append(v)
        if v != s:
            v = way[v]
        else:
            break
    print('Кратчайший путь: ' + ' - '.join(str(x) for x in reversed(res)))


if __name__ == '__main__':
    graph = {
        1: [2, 6],
        2: [3],
        3: [5, 4],
        4: [],
        5: [4],
        6: [2, 3, 5]
    }
    weights = {
        (1, 2): 2,
        (1, 6): 1,
        (2, 3): 2,
        (3, 5): 1,
        (3, 4): 8,
        (5, 4): 1,
        (6, 2): 4,
        (6, 5): 1,
        (6, 3): 4
    }

    s = 1
    t = 4

    way = dijkstra(graph, weights, s, t)
    print_min_way(way, t, s)
