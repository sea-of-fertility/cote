import sys

input = sys.stdin.readline


def solution():
    cnt = int(input())
    roofs = [int(input()) for _ in range(cnt)]
    answer = []
    items = []
    roofs.sort(reverse=True)

    for index, i in enumerate(roofs):
        items.append(i)
        current_weight = items[-1] * len(items)
        answer.append(current_weight)

    print(max(answer))


if __name__ == "__main__":
    solution()