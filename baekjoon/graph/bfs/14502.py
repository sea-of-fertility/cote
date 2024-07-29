import copy
import sys
from collections import deque

input = sys.stdin.readline


dy_dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs():
    global answer
    de = deque()
    arr = copy.deepcopy(graph)

    for row in range(n):
        for col in range(m):
            if arr[row][col] == 2:
                de.append((row, col))

    while de:
        y_x = de.popleft()
        for y, x in dy_dx:
            new_y = y_x[0] + y
            new_x = y_x[1] + x
            if (0 <= new_y < n and 0 <= new_x < m) and arr[new_y][new_x] == 0:
                de.append((new_y, new_x))
                arr[new_y][new_x] = 2

    answer = max(sum(row.count(0) for row in arr), answer)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                graph[row][col] = 1
                make_wall(count+1)
                graph[row][col] = 0


if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    make_wall(0)
    print(answer)
