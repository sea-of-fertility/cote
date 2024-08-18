import sys


input = sys.stdin.readline


def solution(n):
    dp = [[0, 0] for _ in range(91)]
    dp[1] = [0, 1]
    dp[2] = [1, 0]
    dp[3] = [1, 1]
    for index in range(4, n+1):
        front = dp[index - 1]
        dp[index][0] = dp[index][1] = front[0]
        dp[index][0] += front[1]
    print(sum(dp[n]))


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
