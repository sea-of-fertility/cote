def solution(n, k):
    dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
    for row in range(1, n+1):
        for col in range(1, row+1):
            if col == 1:
                dp[row][col] = row
            elif row == col:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col] + dp[row-1][col-1]

    print(dp[n][k] % 10007)


def main():
    n, k = map(int, input().split())
    solution(n, k)


if __name__ == "__main__":
    main()