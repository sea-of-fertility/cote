from collections import deque
import sys

input = sys.stdin.readline
MAX = 100001


def solution():
    de = deque([n])
    route = 0
    while de:
        popleft = de.popleft()
        if popleft == m:
            route += 1
            continue
        go = [popleft - 1, popleft+1, popleft * 2]
        for item in go:

            if MAX > item >= 0 and (0 == place[item] or place[item] == place[popleft] + 1):
                place[item] = place[popleft] + 1
                de.append(item)
    return route


if __name__ == "__main__":
    place = [0 for _ in range(MAX)]
    n, m = map(int, input().split())
    r = solution()
    print(place[m])
    print(r)
