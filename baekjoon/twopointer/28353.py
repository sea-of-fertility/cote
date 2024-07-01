import sys

input = sys.stdin.readline


def solution():
    left = 0
    right = n - 1
    answer = 0
    while left < right:
        weight = arr[left] + arr[right]
        if weight <= k:
            answer += 1
            right -= 1
            left += 1

        else:
            right -= 1

    return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    print(solution())