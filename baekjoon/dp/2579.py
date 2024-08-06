import sys


input = sys.stdin.readline


def solution(stair):
    dp = [0] * len(stair)
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for index in range(3, len(stair)):
        dp[index] = max(dp[index-3] + stair[index-1] + stair[index], dp[index-2] + stair[index])
    print(dp[-1])


def main():
    n = int(input().strip())

    stair = [int(input().strip()) for _ in range(n)]
    print(sum(stair[0:n])) if n <= 2 else solution(stair)


if __name__ == "__main__":
    main()
