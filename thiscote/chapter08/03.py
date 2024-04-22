import sys

input = sys.stdin.readline


def solution():
    for i in range(n):
        if i < 2:
            d[i] = food[i]
        elif 0 <= i - 3:
            d[i] = max(d[i - 3], d[i - 2]) + food[i]


if __name__ == "__main__":
    n = int(input())
    food = list(map(int, input().split()))
    d = [0] * 100
    d[2] = d[1] + food[2]
    solution()
    print(d[n-1])
