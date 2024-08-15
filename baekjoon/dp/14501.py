import sys

input = sys.stdin.readline


def solution(n, arr):
    dp = [0 for _ in range(17)]
    for index in range(n, 0, -1):
        term, weight = arr[index]
        end_day = term + index - 1
        if end_day <= n:
            dp[index] = max(weight + dp[index+term], dp[index-1])
        else:
            dp[index] = dp[index+1]
    print(dp[1])


def main():
    n = int(input())
    arr = [[] for _ in range(n+1)]
    for index in range(1, n+1):
        term, weight = map(int, input().split())
        arr[index] = [term, weight]
    solution(n, arr)


if __name__ == "__main__":
    main()
