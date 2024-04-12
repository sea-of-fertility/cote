import sys

a, b = map(int, sys.stdin.readline().split())
hello = []
answer = []
for i in range(a+b):
    hello.append(sys.stdin.readline().strip())

no_listen = {i: True for i in hello[0:a]}

for i in hello[a:]:
    if i in no_listen:
        answer.append(i)

answer.sort()
print(len(answer))
for i in answer:
    print(i)

