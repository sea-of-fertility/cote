import sys

input = sys.stdin.readline


def solution():
    result = 0
    limit = int((2 * n) ** 0.5) + 1
    for k in range(1, limit):
        if (2 * n - k * (k - 1)) % (2 * k) == 0:
            result += 1

    print(result)


if __name__ == "__main__":
    n = int(input())
    solution()
