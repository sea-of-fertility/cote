import sys
from collections import deque

de = deque()
cnt = int(sys.stdin.readline())
for i in range(cnt):
    word = sys.stdin.readline().strip().split()
    try:
        if word[0] == 'push':

            de.append(word[-1])
        elif word[0] == "pop":
            if len(de) == 0:
                print(-1)
            else:
                print(de.popleft())
        elif word[0] == 'size':
            print(len(de))
        elif word[0] == 'empty':
            if len(de) == 0:
                print(1)
            else:
                print(0)
        elif word[0] == 'front':
            print(de[0])
        elif word[0] == 'back':
            print(de[-1])
    except:
        print(-1)
