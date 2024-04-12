import sys
input = sys.stdin.readline

answer = set()

word = input().strip()
for i in range(1, len(word)+1):
    for l in range(len(word)-i+1):
        answer.add(word[l:l+i])
print(len(answer))