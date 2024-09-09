import sys

input = sys.stdin.readline


def find_dp(dp, arr, row, col):
    if col - arr[0] < 0:
        return dp[row-1][col]
    else:
        return max(dp[row-1][col], dp[row-1][col-arr[0]] + arr[1])


def solution(weight_value, dp):
    for index, arr in enumerate(weight_value):
        for dp_i in range(len(dp[0])):
            dp[index+1][dp_i] = find_dp(dp, arr, index + 1, dp_i)


def main():
    n, k = map(int, input().split())
    weight_value = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    solution(weight_value, dp)
    print(dp[-1][-1])


if __name__ == "__main__":
    main()