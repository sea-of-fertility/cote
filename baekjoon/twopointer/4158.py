from collections import Counter

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cd_list = [int(input()) for _ in range(a+b)]


d = dict(Counter(cd_list))
last_a, last_b = map(int, input().split())
answer = sum(1 for item in d.values() if item == 2)

print(answer)
