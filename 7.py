def BFS(s, t, parent, row, graph_arr):
    queue = []
    queue.append(s)
    visited = [False] * (row)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph_arr[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    if visited[t]:
        return True
    else:
        return False


def method_ford_fulkerson(start, end, row, graph_arr):
    parent = [-1] * (row)
    max = 0
    while BFS(start, end, parent, row, graph_arr):
        path_flow = float("Inf")
        s = end
        while True:
            path_flow = min(path_flow, graph_arr[parent[s]][s])
            s = parent[s]
            if s == start:
                break
        max += path_flow
        v = end
        while True:
            u = parent[v]
            graph_arr[u][v] -= path_flow
            graph_arr[v][u] += path_flow
            v = parent[v]
            if v == start:
                break
    return max, graph_arr


if __name__ == '__main__':
    matrix = [[0, 7, 4, 0, 0, 0],
             [0, 0, 4, 0, 2, 0],
             [0, 0, 0, 8, 4, 0],
             [0, 0, 0, 0, 4, 5],
             [0, 0, 0, 0, 0, 12],
             [0, 0, 0, 0, 0, 0]]
    start = 0
    end = 5
    print("Max: %d " % method_ford_fulkerson(start, end, len(matrix), matrix)[0])
