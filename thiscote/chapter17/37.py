import sys

INF = int(1e9)

input = sys.stdin.readline


def floyd():
    for k in range(1, nodes + 1):
        for a in range(1, nodes + 1):
            for b in range(1, nodes + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if __name__ == "__main__":
    nodes = int(input())
    edges = int(input())

    graph = [[INF for _ in range(nodes + 1)] for _ in range(nodes + 1)]
    for a in range(1, nodes + 1):
        for b in range(1, nodes + 1):
            if a == b:
                graph[a][b] = 0


    for _ in range(edges):
        start_point, end_point, weight = map(int, input().split())
        graph[start_point][end_point] = min(graph[start_point][end_point], weight)
    floyd()

    del graph[0]
    for g in graph:
        del g[0]

    for g in graph:
        for i in g:
            if i != INF:
                print(i, end=" ")
            else:
                print(0, end=" ")
        print()