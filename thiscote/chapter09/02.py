INF = int(1e9)


def floyd():
    for k in range(n + 1):
        for a in range(n + 1):
            for b in range(n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for row in range(n + 1):
        for col in range(n + 1):
            if row == col:
                graph[row][col] = 0

    for _ in range(m):
        start, end = map(int, input().split())

        graph[start][end] = 1
        graph[end][start] = 1
    x, k = map(int, input().split())

    floyd()

    answer = graph[1][k] + graph[k][x]
    print(answer) if answer < 1e9 else print(-1)

    """
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
    
    """
