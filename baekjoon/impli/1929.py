import sys
from math import sqrt

input = sys.stdin.readline


def find_decimal(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution():
    start, end = map(int, input().split())

    for i in range(start, end + 1):
        if find_decimal(i) and i > 1:
            print(i)


if __name__ == "__main__":
    solution()