import sys

N, M = map(int, sys.stdin.readline().split())

word_dict = dict()
answer = 0

for i in range(N):
    a = sys.stdin.readline().strip()
    word_dict[a] = True

for i in range(M):
    a = sys.stdin.readline().strip()
    if a in word_dict:
        answer += 1

print(answer)