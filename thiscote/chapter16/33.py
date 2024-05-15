import sys

input = sys.stdin.readline


def dp():







if __name__ == "__main__":
    t = []
    revenue = []
    n = int(input())
    dp = [[0] * (n + 1)]

    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a)
        revenue.append(b)

