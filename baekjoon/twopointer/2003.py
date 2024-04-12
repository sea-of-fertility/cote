import sys

input = sys.stdin.readline

a, b = map(int, input().split())

numbers = list(map(int, input().strip().split()))
numbers.sort()

print(numbers)


