import sys
from collections import deque
import re

input = sys.stdin.readline


def check(value, save_min):
    if not save_min:
        save_min = [0]
    return value + save_min[0] if value + save_min[0] < value + sum(save_min) else value + sum(save_min)


def solution():
    expression = input().strip()
    numbers = deque(map(int, re.findall(r'-?\d+', expression)))
    answer = 0
    save_plus = 0
    save_min = []
    find_min = False

    while numbers:
        value = numbers.popleft()
        if value > 0:
            save_plus += value
        elif value < 0:
            find_min = True
            save_min.append(value)
            while numbers:
                i = numbers[0]
                if i > 0:
                    save_min.append(-i)
                    numbers.popleft()
                else:
                    break

        if find_min or not numbers:
            answer += check(save_plus, save_min)
            save_min = []
            save_plus = 0
            find_min = False

    print(answer)


if __name__ == '__main__':
    solution()
