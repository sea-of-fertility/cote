import sys


def cumulative_sum(n, m, arr):
    for row in range(1, n+1):
        for col in range(1, m+1):
            arr[row][col] += arr[row][col-1]
    for col in range(1, m+1):
        for row in range(1, n+1):
            arr[row][col] += arr[row-1][col]


def solution(x1, y1, x2, y2, arr):
    return arr[x2][y2] - arr[x1-1][y2] - (arr[x2][y1-1] - arr[x1-1][y1-1])


def main():
    n, m = map(int, input().split())
    arr = [[0] * (m + 1)]
    for _ in range(n):
        arr.append([0] + list(map(int, input().split())))
    cumulative_sum(n, m, arr)

    count = int(input())
    for _ in range(count):
        x1, y1, x2, y2 = map(int, input().split())
        print(solution(x1, y1, x2, y2, arr))


if __name__ == "__main__":
    main()
