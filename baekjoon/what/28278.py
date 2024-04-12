import sys
from collections import deque


cnt = int(sys.stdin.readline())
de = deque()

for i in range(cnt):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        de.append(order[-1])
    elif order[0] == 2:
        if de:
            print(de.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(de))
    elif order[0] == 4:
        if de:
            print(0)
        else:
            print(1)
    elif order[0] == 5:
        if de:
            print(de[-1])
        else:
            print(-1)
