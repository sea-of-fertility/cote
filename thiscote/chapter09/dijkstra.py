INF = int(1e9)


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, nodes + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra():
    visited[start] = True
    distance[start] = 0
    for index, value in enumerate(graph[start]):
        if value != INF:
            distance[index] = value
    for _ in range(nodes - 1):
        now = get_smallest_node()
        visited[now] = True

        for index, value in enumerate(graph[now]):
            cost = distance[now] + value
            if cost < distance[index]:
                distance[index] = cost


if __name__ == "__main__":

    nodes, edge = map(int, input().split())
    start = int(input())
    graph = [[INF for i in range(nodes + 1)] for _ in range(nodes + 1)]

    visited = [False for _ in range(nodes + 1)]
    distance = [INF for i in range(nodes + 1)]

    for _ in range(edge):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    dijkstra()

    for i in range(1, nodes + 1):
        print(f"distance: {distance[i]}") if distance[i] != INF else print("no path")

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

"""