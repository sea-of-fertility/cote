import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(maps):
    answer = 0
    de = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 0:
                de.append([y, x])
                while de:
                    c_y, c_x = de.popleft()
                    for i in range(4):
                        if 0 <= c_y+dy[i] < len(maps) and 0 <= c_x+dx[i] < len(maps[0]) and maps[c_y+dy[i]][c_x+dx[i]] == 0:
                            de.append([c_y+dy[i], x+dx[i]])
                            maps[c_y + dy[i]][c_x + dx[i]] = 1
                answer += 1
    return answer


def solution(maps):
    answer = dfs(maps)


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = []
    for i in range(n):
        maps.append(list(map(int, input().strip())))
    solution(maps)
