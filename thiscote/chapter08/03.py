import sys

input = sys.stdin.readline


def solution():
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + food[i])


if __name__ == "__main__":
    n = int(input())
    food = list(map(int, input().split()))
    d = [0] * 100
    d[0] = food[0]
    d[1] = max(food[0], food[1])
    solution()
    print(d[n-1])
