from math import gcd
import sys

input = sys.stdin.readline

def solution():
    cnt = int(input())
    for _ in range(cnt):
        a, b = map(int, input().split())
        print(a * b // gcd(a,b))


if __name__ == "__main__":
    solution()