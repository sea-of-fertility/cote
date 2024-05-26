import sys

input = sys.stdin.readline


def solution():
    answer = 1
    for index, value in clo.items():
        check = len(value) + 1
        answer *= check

    return  answer - 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        cloth = int(input())
        clo = dict()
        for _ in range(cloth):
            a, b = input().split()
            if b not in clo:
                clo[b] = [a]
            else:
                clo[b].append(a)
        print(solution())