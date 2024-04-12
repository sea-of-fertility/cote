import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v, graph, visit):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i, graph, visit)


def solution():
    n, m = map(int, input().strip().split())

    nodes = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().strip().split())
        nodes[a].append(b)
        nodes[b].append(a)
    answer = 0
    for i in range(1, n + 1):
        if not visit[i]:
            dfs(i, nodes, visit)
            answer += 1

    print(answer)


if __name__ == "__main__":
    solution()