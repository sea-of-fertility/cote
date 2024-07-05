import sys


input = sys.stdin.readline


def cumulative():
    cumulative_sum = [0 for _ in range(n+1)]
    for index, item in enumerate(arr):
        cumulative_sum[index+1] = cumulative_sum[index] + item
    return cumulative_sum


def solution(i, j):
    print(cumulative_sum[j] - cumulative_sum[i-1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cumulative_sum = cumulative()
    for _ in range(m):
        start, end = map(int, input().split())
        solution(start, end)