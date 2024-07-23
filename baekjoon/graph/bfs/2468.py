import copy
import sys
from collections import deque

input = sys.stdin.readline

dx_dy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(arr, row, col, rain):
    de = deque()
    de.append([row, col])
    arr[row][col] = rain
    while de:
        y, x = de.popleft()
        for dy, dx in dx_dy:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < n and 0 <= new_x < n and arr[new_y][new_x] > rain:
                arr[new_y][new_x] = rain
                de.append([new_y, new_x])


def solution(arr, rain):
    result = 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] > rain:
                result += 1
                bfs(arr, row, col, rain)
    return result


if __name__ == "__main__":
    answer = 0
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_height = max(max(row) for row in graph)
    for water in range(max_height+1):
        answer = max(answer, solution(copy.deepcopy(graph), water))
    print(answer)
