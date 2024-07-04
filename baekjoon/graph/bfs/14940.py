import sys
from collections import deque

input = sys.stdin.readline
dy_dx = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def find_goal():
    result = ()
    for col, arr in enumerate(graph):
        for row, item in enumerate(arr):
            if item == 2:
                result = (col, row)
                answer[col][row] = 0
            elif item == 0:
                answer[col][row] = 0
            else:
                answer[col][row] = -1
    return result


def bfs(goal):
    de = deque([goal])
    while de:
        y, x = de.popleft()
        for d in dy_dx:
            dy = y + d[0]
            dx = x + d[1]
            if 0 <= dy < n and 0 <= dx < m:
                if answer[dy][dx] == -1:
                    answer[dy][dx] = answer[y][x] + 1
                    de.append([dy, dx])


def solution():
    goal = find_goal()

    bfs(goal)
    for row in answer:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = [[-1 for _ in range(m)] for _ in range(n)]
    solution()

