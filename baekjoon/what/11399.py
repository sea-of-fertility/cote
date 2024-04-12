import sys

input = sys.stdin.readline

cur_time = 0
time = 0
throw = input()

people = list(map(int, input().split()))
people.sort()

for i in people:
    cur_time += i
    time += cur_time
print(time)

