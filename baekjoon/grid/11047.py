import sys

input = sys.stdin.readline


def solution():
    answer = 0
    n, k = map(int, input().split())

    money = [int(input().strip())for _ in range(n)]
    while money:
        high_coin = money.pop()
        if high_coin <= k:
            d, k = divmod(k, high_coin)
            answer += d
    print(answer)


if __name__ == '__main__':
    solution()
