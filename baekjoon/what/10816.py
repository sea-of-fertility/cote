import sys
from collections import Counter


def solution():
    answer = []
    throw = int(sys.stdin.readline())
    n_dict = dict(Counter(map(int, sys.stdin.readline().split())))

    throw = int(sys.stdin.readline())
    check = list(map(int, sys.stdin.readline().split()))
    for i in check:
        if i in n_dict:
            print(n_dict[i], end=" ")
        else:
            print(0, end=" ")


if __name__ == "__main__":
    solution()