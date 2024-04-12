import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def bfs(v, graph, visit):
    visit[v] = 0
    cnt = 1
    answer = [0 for _ in range(len(graph) + 1)]
    answer[v] = 0
    de = deque()
    de.append(v)
    while de:
        v = de.popleft()
        for i in graph[v]:
            if visit[i] == -1:
                de.append(i)
                visit[i] = visit[v] + 1
                cnt += 1
                answer[i] = visit[i] * cnt

    return answer



def solution():
    node, edge, v = map(int, input().split())
    visit = [-1 for _ in range(node + 1)]
    graph = [[] for _ in range(node + 1)]
    for _ in range(edge):
        n, m = map(int, input().split())
        graph[n].append(m)
        graph[m].append(n)

    for i in graph:
        i.sort(reverse=False)
    l = bfs(v, graph, visit)
    print(sum(l))


if __name__ == "__main__":
    solution()
