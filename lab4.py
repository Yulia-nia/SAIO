
def topological_sort(g, start, stop):
    stack = []
    items_set = []
    order = []
    q = [start, stop]
    while q:
        v = q.pop()
        if v not in items_set:
            q.extend(g[v][0])
            while True:
                if stack and v not in g[stack[-1]][0]:
                    order.append(stack.pop())
                else:
                    break
            items_set.append(v)
            stack.append(v)
    return stack + order[::-1]


def max_way(graph, s, t):
    topological_list = topological_sort(graph, s, t)  # пунк 1
    print('Результат упорядочивание вершин: {}'.format(topological_list))
    start_list_way = dict([(i, 0) for i in topological_list])
    f = [0]
    for i in range(len(topological_list) - 1):
        v2, sums = topological_list[i + 1], []
        possible_way = []
        for k, v in graph.items():
            if v2 in v[0]:
                index = v[0].index(v2)
                possible_way.append([k, v[1][index]])
        for item in possible_way:
            sum = start_list_way[item[0]] + item[1]
            sums.append([sum, item[0]])
        sums.sort()
        start_list_way[v2] = sums[-1][0]
        f.append(sums[-1][1])
    print('Максимальный вес: ', list(start_list_way.values())[-1])
    path, l_keys = [], list(start_list_way.keys())
    current_key = t
    while True:
        path.append(current_key)
        index = l_keys.index(current_key)
        if f[index] == 0:
            break
        current_key = f[index]
        del l_keys[index]
    path.reverse()
    print('Оптимальный путь: ' + ' - '.join(str(x) for x in path))


if __name__ == '__main__':
    graph = {
        1: [[2, 6],
            [2, 1]],
        2: [[3],
            [2]],
        3: [[5, 4],
            [1, 8]],
        4: [[],
            []],
        5: [[4],
            [1]],
        6: [[2, 3, 5],
            [4, 5, 1]]
    }
    s = 1
    t = 4
    max_way(graph, s, t)
