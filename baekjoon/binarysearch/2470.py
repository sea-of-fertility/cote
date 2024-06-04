import sys

input = sys.stdin.readline
INF = sys.maxsize


def solution():
    min_value = INF
    answer = []

    for index in range(len(arr) - 1):
        cur_value = arr[index]
        start = arr[index + 1]
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            num = cur_value + arr[mid]

            if abs(min_value) > abs(num):
                min_value = abs(num)
                answer = [arr[index], arr[mid]]

            if num == 0:
                break

            if num > 0:
                if abs(num) > 0:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if abs(num) > 0:
                    start = mid + 1
                else:
                    end = mid - 1

    for item in answer:
        print(item, end=" ")


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    solution()
