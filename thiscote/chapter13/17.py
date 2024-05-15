from collections import deque

d = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def solution():
    de = deque(data)
    while de:

        v, t, my, mx = de.popleft()
        if t < s:
            for move in d:
                dy = my + move[0]
                dx = mx + move[1]
                if -1 < dy < n and -1 < dx < n and t < s:
                    if graph[dy][dx] == 0:
                        graph[dy][dx] = v
                        de.append([v, t + 1, dy, dx])


if __name__ == "__main__":
    data = []
    n, k = map(int, input().split())

    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
        for l in range(n):
            if graph[i][l] != 0:
                data.append([graph[i][l], 0, i, l])
    data.sort()
    s, x, y = map(int, input().split())
    solution()

    print(graph[x - 1][y - 1])

"""

3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""
