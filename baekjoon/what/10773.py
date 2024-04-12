import sys
from collections import deque

de = deque()

cnt = int(sys.stdin.readline())
for i in range(cnt):

    num = int(sys.stdin.readline())

    if num != 0:
        de.append(num)
    else:
        de.pop()

print(sum(de))
