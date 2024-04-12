import sys

input = sys.stdin.readline

pml = []
pmd = dict()
pnd = dict()
n, m = map(int, input().split())
for cnt in range(1, n+1):
    name = input().strip()
    pmd [name] = cnt
    pnd [cnt] = name
for _ in range(m):
    quiz = input().strip()

    if quiz in pmd:
        print(pmd[quiz])
    else:
        print(pnd[int(quiz)])