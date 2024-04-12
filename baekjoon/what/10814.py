import sys

input = sys.stdin.readline


def solution():
    members = []

    cnt = int(input())
    for i in range(cnt):
        list = input().split()
        list[0] = int(list[0])
        list.append(i)
        members.append(list)

    members.sort(key=lambda x: (x[0], x[2]))
    for i in members:
        del i[-1]
        print(i[0], i[1])


if __name__ == '__main__':
    solution()
