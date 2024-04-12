from collections import deque
import sys

de = deque()
count = int(sys.stdin.readline())
for i in range(count):
    order = list(map(str, sys.stdin.readline().split()))
    # print(order)
    front_order = order[0]
    back_order = order[-1]

    if back_order.isdigit():
        if order[0] == "push_front":
            de.appendleft(int(order[-1]))
        else:
            de.append(int(order[-1]))

    elif front_order == "size":
        print(len(de))

    elif front_order == "front":
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])

    elif front_order == "back":
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])

    elif front_order == "empty":
        if len(de) == 0:
            print(1)
        else:
            print(0)

    elif front_order.startswith("pop"):
        try:
            if "front" in front_order:
                print(de.popleft())
            else:
                print(de.pop())
        except:
            print(-1)