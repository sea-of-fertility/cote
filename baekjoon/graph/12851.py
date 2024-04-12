import sys
from collections import deque


input = sys.stdin.readline


def bfs(s, d, move):
    qu = deque([s])
    lim = 100000
    answer = 0
    while qu:
        node = qu.popleft()
        go = [node - 1, node + 1, node * 2]
        for i in go:
            if 0 <= i <= 100000 and move[node] <= lim:
                if i not in move:
                    move[i] = move[node] + 1
                    qu.append(i)
                if d == i:
                    lim = move[i]
                    answer += 1
    return answer


def check_same_location(start, destination):
    if start == destination:
        print(0)
        print(1)
        return True
    else:
        return False


def solution():
    start, destination = map(int, input().split())

    if check_same_location(start, destination):
        return

    move = dict()
    move[start] = 0
    answer = bfs(start, destination, move)
    print(move[destination])
    print(answer)


if __name__ == "__main__":
    solution()
