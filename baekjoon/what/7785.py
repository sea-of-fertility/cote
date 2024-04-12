import sys


input = sys.stdin.readline


x = int(input().strip())
answer = 0

log_dict = set()

for i in range(x):
    log = list((input().split()))
    if log[-1] == 'enter':
        log_dict.add(log[0])
    else:
        log_dict.remove(log[0])

answer = sorted(log_dict, reverse=True)
for name in answer:
    print(name)
