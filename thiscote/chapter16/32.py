import sys

input = sys.stdin.readline

search = (-1, 0)


def solution():
    for i in range(1, size):
        for index, item in enumerate(dp[i]):
            max_item = 0
            for d in search:
                if -1 < index + d < len(dp[i - 1]):
                    if max_item < dp[i - 1][index+d]:
                        max_item = dp[i - 1][index + d]
            dp[i][index] += max_item


if __name__ == "__main__":

    size = int(input())

    dp = []

    for index in range(size):
        dp.append(list(map(int, input().split())))

    solution()
    print(max(dp[-1]))