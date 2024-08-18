import sys
arr_len = int(1e6) + 1

input = sys.stdin.readline


def solution(n):
    dp = [0] * arr_len
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for index in range(4, n+1):
        dp[index] = (dp[index-1] + dp[index-2])%15746
    print(dp[n])


def main():
    n = int(input())
    print(n) if n <= 3 else solution(n)


if __name__ == "__main__":
    main()