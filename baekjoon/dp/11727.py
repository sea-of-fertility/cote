def solution(n):
    dp = [0] * 1001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for index in range(3, n+1):
        dp[index] = dp[index-1] + dp[index-2] * 2
    print(dp[n] % 10007)


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
