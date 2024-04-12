import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, destin):
    node = dict()
    de = deque()
    de.append(start)
    node[start] = 0
    while de:
        if destin in node:
            return node[destin]
        v = de.popleft()

        if v - 1 not in node and v - 1 >= 0:
            node[v - 1] = node[v] + 1
            de.append(v - 1)
        if v * 2 not in node and v*2 <= 100000:
            node[v * 2] = node[v]
            de.append(v * 2)
        if v + 1 not in node:
            node[v + 1] = node[v] + 1
            de.append(v + 1)


def solution():
    a, b = map(int, input().split())
    i = bfs(a, b)
    print(i)


if __name__ == "__main__":
    solution()
