import sys
from collections import deque


dy_dx = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def find_tomato():
    de = deque()
    for col, arr in enumerate(graph):
        for row, item in enumerate(arr):
            if item == 1:
                de.append((col, row))
    return de


def check():
    for col, arr in enumerate(graph):
        for row, item in enumerate(arr):
            if item == 0:
                return True
    return False


def solution():
    answer = 0
    de = find_tomato()
    while de:
        y, x = de.popleft()
        for d in dy_dx:
            new_y = y + d[0]
            new_x = x + d[1]
            if (0 <= new_y < n and 0 <= new_x < m) and graph[new_y][new_x] == 0:
                graph[new_y][new_x] = graph[y][x] + 1
                answer = graph[new_y][new_x]
                de.append((new_y, new_x))
    if check():
        print(-1)
    elif answer == 0:
        print(answer)
    else:
        print(answer - 1)


if __name__ == "__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution()
