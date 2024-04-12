import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def dfs(v, graph, visit, cnt):
    visit[v] = cnt

    for i in graph[v]:
        if visit[i] == 0:
            cnt = dfs(i, graph, visit, cnt+1)
    return cnt


def solution():
    nodes, edge, v = map(int, input().split())
    graph = [[] for _ in range(nodes+1)]
    visit = [0] * (nodes+1)
    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, nodes + 1):
        graph[i].sort(reverse=True)

    cnt = 1
    dfs(v, graph, visit, cnt)

    for item in visit[1:]:
        print(item)


if __name__ == "__main__":
    solution()
