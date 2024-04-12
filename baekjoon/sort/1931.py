import sys

input = sys.stdin.readline


def solution():
    cnt = int(input())

    time = [list(map(int, input().split())) for i in range(cnt)]
    time.sort(key=lambda x:(x[1] - x[0], x[0]))
    print(time)


if __name__ == "__main__":
    solution()