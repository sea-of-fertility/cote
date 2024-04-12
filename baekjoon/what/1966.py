import sys
from collections import deque

cnt = int(sys.stdin.readline())

for i in range(cnt):
    que_len, target = map(int, sys.stdin.readline().split())
    pro = list((map(int, sys.stdin.readline().split())))
    que = deque([location, value] for location, value in enumerate(pro))
    answer = 0
    while True:
        cur = que.popleft()
        if any(cur[1] < q[1] for q in que):
            que.append(cur)
        else:
            answer += 1
            if cur[0] == target:
                print(answer)
                break
