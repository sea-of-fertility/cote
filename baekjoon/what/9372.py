import sys
from collections import deque

input = sys.stdin.readline

def bfs(v, graph):
    de = deque([v])
    visit = [v]
    cnt = 0
    while de:
        v = de.popleft()
        for i in graph[v]:
            if i not in visit:
                cnt += 1
                visit.append(i)
                de.append(i)
    return cnt


def solution():
    t = int(input())

    for i in range(t):
        node, edge = map(int, input().split())
        graph = [[] for i in range(node + 1)]

        for _ in range(edge):
            node1, node2 = map(int, input().split())
            graph[node1].append(node2)
            graph[node2].append(node1)

        print(bfs(1, graph))


if __name__ == '__main__':
    solution()
