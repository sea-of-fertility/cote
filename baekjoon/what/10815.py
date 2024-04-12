import sys

throw1 = sys.stdin.readline()
card_dict = set(map(int, sys.stdin.readline().split()))

throw2 = sys.stdin.readline()
check = list(map(int, sys.stdin.readline().split()))
for i in check:
    if i in card_dict:
        print(1, end=" ")
    else:
        print(0, end=" ")




