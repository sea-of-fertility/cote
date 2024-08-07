import sys


input = sys.stdin.readline


def solution(n, arr):
    dp = [0] * n
    dp[0] = arr[0]
    for index in range(1, n):
        dp[index] = max(dp[index-1] + arr[index], arr[index])
    print(max(dp))


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solution(n, arr)


if __name__ == "__main__":
    main()
