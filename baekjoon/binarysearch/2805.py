import sys

input = sys.stdin.readline


def findCut(num):
    result = 0
    for item in arr:
        if item >= num:
            result += item - num
    return result


def binarySearch():
    start = 0
    end = arr[-1]

    while start <= end:
        mid = (start + end) // 2
        find = findCut(mid)
        if find == m:
            print(mid)
            return
        elif find > m:
            start = mid + 1
        else:
            end = mid - 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    binarySearch()
