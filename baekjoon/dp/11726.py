dp = [0, 1, 2] + [0 for _ in range(998)]


def solution(n):
    for index in range(3, n+1):
        dp[index] = dp[index-1] + dp[index-2]
    print(dp[n] % 10007)


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()