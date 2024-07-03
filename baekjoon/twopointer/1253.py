import sys

input = sys.stdin.readline


def two_pointer(tmp, target):
    left = 0
    right = n - 2
    global answer
    while left < right:
        value = tmp[left] + tmp[right]
        if value == target:
            answer += 1
            return
        elif value > target:
            right -= 1
        else:
            left += 1


def solution():
    for i in range(n):
        tmp = arr[:i] + arr[i + 1:]
        two_pointer(tmp, arr[i])


if __name__ == "__main__":
    answer = 0
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    dic = {item: True for item in arr}
    solution()
    print(answer)
