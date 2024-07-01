import sys


input = sys.stdin.readline


def solution():
    cur_value = sum(arr[:k])
    max_value = cur_value
    for index in range(n-k):
        cur_value = cur_value - arr[index] + arr[index+k]
        max_value = max(cur_value, max_value)

    return max_value


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution())