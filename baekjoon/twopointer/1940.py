import sys


input = sys.stdin.readline


def two_pointer():
    left = 0
    right = n - 1
    count = 0
    while left < right:
        sum_value = arr[left] + arr[right]
        if sum_value < target:
            left += 1
        elif sum_value > target:
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1
    return count


if __name__ == "__main__":
    n = int(input())
    target = int(input())
    arr = sorted(list(map(int, input().split())))
    print(two_pointer())
