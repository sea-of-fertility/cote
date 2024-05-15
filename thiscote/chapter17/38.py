INF = int(1e9)


def floyd():
    for k in range(1, n+1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if __name__ == "__main__":

    n, m = map(int, input().split())

    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for l in range(1, n+1):
            if i == l:
                graph[i][l] = 0
                break

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s][e] = 1
    floyd()

    print(graph)

    


"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""