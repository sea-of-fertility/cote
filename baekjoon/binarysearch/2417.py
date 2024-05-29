import sys

input = sys.stdin.readline


def solution():
    end = int(2e33)
    start = 0
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 < n:
            start = mid + 1
        else:
            end = mid - 1
    print(start)


if __name__ == "__main__":
    n = int(input())
    solution()