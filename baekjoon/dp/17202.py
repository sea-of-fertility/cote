import sys

input = sys.stdin.readline


def solution():
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))
    dp = [[0] * (16 - i) for i in range(16)]

    for i in range(8):
        dp[2 * i] = a[i]
        dp[2 * i + 1] = b[i]

    for i in range(1, 16):
        for l in range(len(dp[i])):
            dp[i][l] = (dp[i - 1][l] + dp[i - 1][l + 1]) % 10
    print(f'{dp[-2][0]}{dp[-2][1]}')


if __name__ == "__main__":
    solution()
