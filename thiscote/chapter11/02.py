import sys

input = sys.stdin.readline


def solution(value):
    for i in arr[1:]:
        if i < 2:
            value += i
        else:
            value *= i
    return value


if __name__ == "__main__":
    arr = list(map(int, input().strip()))

    for index, item in enumerate(arr):
        if item == 0:
            del arr[index]

    answer = arr[0]

    print(solution(answer))
