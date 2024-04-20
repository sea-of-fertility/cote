from collections import deque


def solution():
    while de:
        popleft = de.popleft()
        for i in coins:
            new_coin = popleft + i
            if new_coin <= m and coin_list[new_coin] == -1:
                coin_list[new_coin] = coin_list[popleft] + 1
                de.append(new_coin)


if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    coin_list = [-1 for i in range(m + 1)]
    for i in coins:
        if i < m:
            coin_list[i] = 1
    de = deque(coins)
    solution()
    print(coin_list)