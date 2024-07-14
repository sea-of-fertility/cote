import sys


def find(num):
    check = 1
    total = 0
    for item in arr:
        if total + item <= num:
            total += item
        else:
            check += 1
            total = item
    return check


def solution():
    result = 0
    start = max(arr)
    end = sum(arr)
    while start <= end:
        mid = (start + end) // 2
        if find(mid) > m:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    print(result)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    solution()