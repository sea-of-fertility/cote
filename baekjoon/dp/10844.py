import sys

m = int(1e9)

input = sys.stdin.readline


def solution(n):
    dp = [[0 for _ in range(10)] for _ in range(101)]
    dp[1] = [1 for _ in range(10)]
    dp[1][0] = 0
    dp[2] = [2 for _ in range(10)]
    dp[2][0] = 0
    dp[2][-1] = 1
    for row in range(3, 101):
        for col in range(1, 10):
            if col == 1:
                dp[row][col] = dp[row-1][col+1] + dp[row-2][col]
            elif col == 9:
                dp[row][col] = dp[row-1][8]
            else:
                dp[row][col] = dp[row-1][col-1] + dp[row-1][col+1]
    print(sum(dp[n]) % m)

def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
