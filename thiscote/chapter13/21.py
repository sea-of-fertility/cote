from collections import deque

d = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def solution():
    answer = 0
    evg = 0
    for col in range(n):
        for row in range(n):
            if graph[col][row] != evg:

                de = deque()
                de.append([graph[col][row], col, row])
                visit = [[False for _ in range(n)] for _ in range(n)]
                check = []

                while de:
                    value, y, x = de.popleft()

                    for dy, dx in d:
                        dy += y
                        dx += x
                        if -1 < dy < n and -1 < dx < n:
                            if l <= abs(graph[dy][dx] - value) <= r and not visit[dy][dx]:
                                de.append([graph[dy][dx], dy, dx])
                                visit[dy][dx] = True
                                evg += graph[dy][dx]
                                check.append([dy, dx])

                if check:
                    evg //= len(check)
                    answer += 1
                for y, x in check:
                    graph[y][x] = evg
    return answer


if __name__ == "__main__":
    n, l, r = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    print(graph)
    a = solution()
    print(graph)
    print(a)
