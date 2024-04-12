import sys
from collections import deque


def solution():
    N, K = map(int, sys.stdin.readline().split())
    people = [i for i in range(1, N + 1)]
    answer = []
    idx = 0
    while len(people) > 0:
        idx = (idx + K - 1) % len(people)
        print(idx)
        answer.append(str(people.pop(idx)))
    print('<', ', '.join(answer), '>', sep='')


if __name__ == '__main__':
    solution()
