import sys
from collections import deque

dy_dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(y, x):
    de = deque()
    de.append((y, x))
    graph[y][x] = 0
    result = 1
    while de:
        c_y, c_x = de.popleft()
        for move in dy_dx:
            new_dy = c_y + move[0]
            new_dx = c_x + move[1]
            if (0 <= new_dx < len(graph[0]) and 0 <= new_dy < n) and graph[new_dy][new_dx] != 0:
                result += 1
                graph[new_dy][new_dx] = 0
                de.append((new_dy, new_dx))
    answer.append(result)


if __name__ == "__main__":
    n = int(input())
    graph = []
    answer = []
    count = 0
    for _ in range(n):
        graph.append(list(map(int, input())))
    for row in range(n):
        for col in range(len(graph[0])):
            if graph[row][col] != 0:
                bfs(row, col)

    print(len(answer))
    for ans in sorted(answer):
        print(ans)
