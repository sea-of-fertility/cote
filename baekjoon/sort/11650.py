import sys

input = sys.stdin.readline


def solution():
    cnt = int(input())

    points = [list(map(int, input().strip().split())) for i in range(cnt)]
    points.sort(key=lambda x:(x[0], x[1]))

    for i in points:
        print(i[0], i[1])


if __name__ == "__main__":
    solution()
