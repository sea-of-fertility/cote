import sys


input = sys.stdin.readline


def backpack(dp, row, col, l, k):
    if col - k < 0:
        return dp[row - 1][col]
    else:
        return max(dp[row - 1][col], dp[row - 1][col - k] + l)


def solution(dp, l_t_list):
    for row, l_t in enumerate(l_t_list):
        for col in range(len(dp[0])):
            dp[row +1][col] = backpack(dp, row + 1, col, l_t[0], l_t[1])


def main():
    n, k = map(int, input().split())
    l_t = [list(map(int, input().split())) for _ in range(k)]
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    solution(dp, l_t)
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
