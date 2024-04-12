import sys
from collections import deque

input = sys.stdin.readline
#   right, down, up, left
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]


def bfs(maps):
    de = deque()
    de.append([0, 0])
    while de:
        cur_y, cur_x = de.popleft()
        for i in range(4):
            to_x = cur_x + dx[i]
            to_y = cur_y + dy[i]
            if 0 <= to_x < len(maps[0]) and 0 <= to_y < len(maps) and maps[to_y][to_x] == 1:
                maps[to_y][to_x] = maps[cur_y][cur_x] + 1
                de.append([to_y, to_x])


def solution():
    y, x = map(int, input().split())
    graph = []
    for _ in range(y):
        graph.append(list(map(int, input().strip())))
    bfs(graph)
    print(graph[y-1][x-1])


if __name__ == "__main__":
    solution()