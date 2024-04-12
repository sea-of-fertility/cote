import sys
from collections import Counter

input = sys.stdin.readline


def solution():
    cnt = int(input())
    num = [int(input()) for _ in range(cnt)]
    num_dict = dict(Counter(num))
    max_item = max(num_dict.values())
    frequency = [key for key, item in num_dict.items() if item == max_item]
    frequency.sort()
    num.sort()
    print(int(round(sum(num)/len(num), 0)))
    print(num[len(num)//2])
    print(frequency[1] if len(frequency) > 1 else frequency[0])
    print(num[-1]- num[0])


if __name__ == "__main__":
    solution()