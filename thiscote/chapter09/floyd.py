INF = int(1e9)


def floyd():
    for k in range(1, nodes+1):
        for a in range(1, nodes+1):
            for b in range(1, nodes+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if __name__ == "__main__":
    nodes = int(input())
    edge = int(input())

    graph = [[INF for _ in range(nodes+1)] for _ in range(nodes+1)]

    for row in range(1, nodes+1):
        for col in range(1, nodes+1):
            if row == col:
                graph[row][col] = 0

    for _ in range(edge):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight

    floyd()

    for row in range(1, nodes+1):
        for col in range(1, nodes+1):
            if graph[row][col] != INF:
                print(graph[row][col], end=" ")
        print()


"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""