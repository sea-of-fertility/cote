def dp(coins, k):
    dp_tables = [0 for _ in range(k+1)]
    dp_tables[0] = 1
    for coin in coins:
        for col in range(k+1):
            if col >= coin:
                dp_tables[col] = dp_tables[col-coin] + dp_tables[col]

    print(dp_tables[-1])


def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp(coins, k)


if __name__ == "__main__":
    main()
