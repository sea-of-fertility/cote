import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def dfs(v, graph, visit, depth, search):
    visit[v] = depth * search

    for i in graph[v]:
        if visit[i] == -1:
            search = dfs(i, graph, visit, depth+1, search + 1)
    return search


def solution():
    nodes, edge, v = map(int, input().split())
    graph = [[] for _ in range(nodes + 1)]
    visit = [-1] * (nodes + 1)
    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, nodes + 1):
        graph[i].sort(reverse=True)

    depth = 0
    search = 1
    dfs(v, graph, visit, depth, search)
    answer = 0

    for i in visit[1:]:
        if i > -1:
            answer += i
    print(answer)


if __name__ == "__main__":
    solution()
