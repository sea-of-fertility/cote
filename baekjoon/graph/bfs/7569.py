import sys
from collections import deque


input = sys.stdin.readline


dy_dx = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [-1, 0, 0], [1, 0, 0]]


def find_tomato():
    de = deque()
    for high in range(h):
        for row in range(m):
            for col in range(n):
                if graph[high][row][col] == 1:
                    de.append((high, row, col))
    return de


def solution():
    de = find_tomato()
    day = 0
    while de:
        tomato = de.popleft()
        for dz, dy, dx in dy_dx:
            new_z = tomato[0] + dz
            new_y = tomato[1] + dy
            new_x = tomato[2] + dx
            if (0 <= new_z < h and 0 <= new_y < m and 0 <= new_x < n) and graph[new_z][new_y][new_x] == 0:
                de.append((new_z, new_y, new_x))
                graph[new_z][new_y][new_x] = graph[tomato[0]][tomato[1]][tomato[2]] + 1
                day = graph[new_z][new_y][new_x]
    for high in range(h):
        for row in range(m):
            for col in range(n):
                if graph[high][row][col] == 0:
                    print(-1)
                    return
    day -= 1
    print(day if day > 0 else 0)


if __name__ == "__main__":
    n, m, h = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
    solution()
