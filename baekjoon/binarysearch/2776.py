import sys

input = sys.stdin.readline


def solution():
    answer = dict()
    for item in one:
        answer[item] = 1
    for value in two:
        if value in answer:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = input()
        one = list(map(int, input().split()))
        one.sort()
        b = input()
        two = list(map(int, input().split()))
        solution()
