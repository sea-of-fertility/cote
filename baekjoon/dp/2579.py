import sys


input = sys.stdin.readline


def solution(arr):
    answer = sum(arr)
    index = len(arr) - 1

    while index > 1:
        if arr[index-1] < arr[index-2]:
            value = arr[index-1]
            index -= 2
        else:
            value = arr[index-2]
            index -= 3
        answer -= value

    print(answer)


def main():
    n = int(input().strip())
    dp = [int(input().strip()) for _ in range(n)]
    solution(dp)


if __name__ == "__main__":
    main()
