import sys

input = sys.stdin.readline


def solution():
    cnt = int(input())
    word = [input().strip() for _ in range(cnt)]
    word = list(set(word))
    word.sort(key = lambda x:(len(x), x))

    for i in word:
        print(i)


if __name__ == '__main__':
    solution()
