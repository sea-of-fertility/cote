import sys

input = sys.stdin.readline

INF = int(1e7)


def solution(k, coin_type):
    dp = init(len(coin_type), k)
    for row, coin in enumerate(coin_type, start=1):
        for col in range(k+1):
            if col < coin:
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = min(dp[row-1][col], dp[row][col-coin] + 1)

    print(-1) if dp[-1][-1] >= INF else print(dp[-1][-1])


def init(n, k):
    dp = [[INF for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 0
    return dp


def main():
    n, k = map(int, input().split())
    coin_type = [int(input()) for _ in range(n)]
    solution(k, coin_type)


if __name__ == "__main__":
    main()
