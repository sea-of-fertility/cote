import sys
from collections import deque


input = sys.stdin.readline


def bfs(s, d, move):
    qu = deque([s])
    while qu:
        node = qu.popleft()
        go = [node - 1, node + 1, node * 2]
        for i in go:
            if 0 <= i <= 100000 and i not in move:
                move[i] = move[node] + 1
                if i == d:
                    return
                qu.append(i)


def check_same_location(start, destination):
    if start == destination:
        print(0)
        print(start)
        return True
    else:
        return False


def solution():
    start, destination = map(int, input().split())
    if check_same_location(start, destination):
        return
    move = dict()
    move[start] = 0
    bfs(start, destination, move)
    print(move[destination])



if __name__ == "__main__":
    solution()