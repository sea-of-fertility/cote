from collections import deque

import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(graph):
    de = deque()
    answer = 0
    for index, g in enumerate(graph):
        for i, node in enumerate(g):
            if node != 0:
                de.append([index, i])
                while de:
                    cur_y, cur_x = de.popleft()
                    for move in range(8):
                        x = cur_x + dx[move]
                        y = cur_y + dy[move]
                        if len(graph[0]) > x >= 0 and 0 <= y < len(graph) and graph[y][x] == 1:
                            graph[y][x] = 0
                            de.append([y, x])
                answer += 1
    return answer


def solution():
    while True:
        a, b = map(int, input().split())
        if a == 0 or b == 0:
            break
        else:
            maps = [list(map(int, input().strip().split())) for _ in range(b)]
            print(bfs(maps))


if __name__ == "__main__":
    solution()
