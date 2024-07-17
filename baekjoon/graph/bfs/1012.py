import sys
from collections import deque

input = sys.stdin.readline

dx_dy = [[1, 0], [0, 1], [-1, 0],[0, -1]]


def bfs(col, row):
    de = deque([(col, row)])  # Using tuple here
    while de:
        dy, dx = de.popleft()
        graph[dy][dx] = False
        for d in dx_dy:
            new_dy = dy + d[0]
            new_dx = dx + d[1]
            if 0 <= new_dy < n and 0 <= new_dx < m and graph[new_dy][new_dx]:
                graph[new_dy][new_dx] = False
                de.append((new_dy, new_dx))


def solution():
    answer = 0
    for col in range(n):
        for row in range(m):
            if graph[col][row]:
                bfs(col, row)
                answer += 1
    return answer


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        m, n, k = map(int, input().split())
        graph = [[0 for _ in range(m)] for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = True
        print(solution())
