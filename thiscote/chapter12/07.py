import sys

input = sys.stdin.readline


def solution():
    half_len = len(arr)//2
    arr1 = arr[0:half_len]
    arr2 = arr[half_len:]

    print("LUCKY") if sum(arr1) == sum(arr2) else print("READY")


if __name__ == "__main__":
    arr = list(map(int, input().strip()))

    solution()
