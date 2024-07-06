import sys


input = sys.stdin.readline


def cumulative(cur_sum):
    for index, item in enumerate(arr):
        cur_sum[index+1] = cur_sum[index] + item
    return cur_sum


def solution(i, j):
    print(cumulative_sum[j] - cumulative_sum[i-1])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    cumulative_sum = [0 for _ in range(n+1)]
    cumulative(cumulative_sum)
    for _ in range(m):
        start, end = map(int, input().split())
        solution(start, end)
