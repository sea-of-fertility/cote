import sys

input = sys.stdin.readline


def stack(start, end, mid, result):
    value = 0

    if start > end:
        return result
    for i in arr:
        value += i - mid

    if value == m:
        return mid

    elif value > m:
        result = mid
        return stack(mid, end, (mid + end) // 2, result)
    else:
        return stack(start, mid, (start + mid) // 2, result)


def roof(start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in arr:
            if x > mid:
                total += x - mid

        if total < m:
            end = mid - 1

        else:
            result = mid
            start = mid + 1

    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(roof(arr[0], arr[-1]))

"""
4 6
15 19 10 17
"""
