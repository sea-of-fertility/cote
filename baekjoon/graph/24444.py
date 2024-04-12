import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def bfs(v, graph, visit):
    cnt = 1
    qu = deque()
    qu.append(v)
    visit[v] = cnt
    cnt += 1
    while qu:
        v = qu.popleft()

        for i in graph[v]:
            if visit[i] == 0:
                qu.append(i)
                visit[i] = cnt
                cnt += 1


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
    bfs(v, graph, visit)

    for item in visit[1:]:
        print(item)


if __name__ == "__main__":
    solution()
