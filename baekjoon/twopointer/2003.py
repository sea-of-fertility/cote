import sys


input = sys.stdin.readline


def solution():
    left = 0
    right = 1
    result = 0
    sum_value = arr[0]
    while True:
        if sum_value < target:
            if right < n:
                sum_value += arr[right]
                right += 1
            else:
                break
        elif sum_value == target:
            result += 1
            sum_value -= arr[left]
            left += 1
        else:
            sum_value -= arr[left]
            left += 1
    return result


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = solution()
    print(answer)
