import sys


def dfs(v, graph, check):
    check.append(v)
    for i in graph[v]:
        if i not in check:
            check = dfs(i, graph, check)

    return check


def solution():
    answer = []
    node = int(sys.stdin.readline())
    edge = int(sys.stdin.readline())
    graph = [[] for i in range(0, node + 1)]

    for i in range(edge):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = len(dfs(1, graph, [])) - 1
    print(answer)


if __name__ == "__main__":
    solution()
