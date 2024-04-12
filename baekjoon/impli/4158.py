import sys

input = sys.stdin.readline


def solution():
    answer = list()
    while True:
        a, b = map(int, input().split())
        if a == b and a == 0:
            break
        else:
            cd_dict = {}
            quen = 0
            for i in range(a):
                num = int(input())
                cd_dict[num] = True
            for l in range(b):
                num = int(input())
                if num in cd_dict:
                    quen += 1
        answer.append(quen)

    for a in answer:
        print(a)


if __name__ == "__main__":
    solution()