import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline


def bfs(maps):
    de = deque()
    de.append([0, 0])
    while de:
        y, x = de.popleft()
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if 0 <= n_y < len(maps) and 0 <= n_x < len(maps[0]) and maps[n_y][n_x] == 1:
                maps[n_y][n_x] += maps[y][x]
                de.append([n_y, n_x])


def solution(n, m, maps):
    bfs(maps)
    print(maps)


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = []
    for l in range(n):
        maps.append(list(map(int, input().strip())))
    solution(n, m, maps)
