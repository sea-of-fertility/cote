import copy
import sys
from collections import deque

input = sys.stdin.readline

dy_dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

colors = ['R', 'G', 'B']


def bfs(n, graph, row, col):
    target = graph[row][col]
    de = deque()
    de.append((row, col))
    while de:
        y_x = de.popleft()
        for dy, dx in dy_dx:
            new_y = y_x[0] + dy
            new_x = y_x[1] + dx
            if 0 <= new_y < n and 0 <= new_x < n and graph[new_y][new_x] == target:
                de.append((new_y, new_x))
                graph[new_y][new_x] = "X"


def find_section(n, graph):
    result = 0
    for row in range(n):
        for col in range(n):
            if graph[row][col] in colors:
                result += 1
                bfs(n, graph, row, col)
    print(result)


def normal(n, graph):
    find_section(n, graph)


def set_picture(n, graph):
    graph[:] = [['G' if cell == 'R' else cell for cell in row] for row in graph]


def color_blindness(n, graph):
    set_picture(n, graph)
    find_section(n, graph)


def main():
    n = int(input())
    picture = [list(input()) for _ in range(n)]
    normal(n, copy.deepcopy(picture))
    color_blindness(n, copy.deepcopy(picture))


if __name__ == "__main__":
    main()
