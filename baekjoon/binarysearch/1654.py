import sys

input = sys.stdin.readline


def find_quantity(num):
    return sum(item // num for item in line)


def solution():
    end = line[-1]
    start = 1
    answer = 0
    while start <= end:
        mid = (end + start) // 2
        find = find_quantity(mid)
        if find >= m:
            start = mid + 1
            answer = mid

        else:
            end = mid - 1
    print(answer)


if __name__ == "__main__":
    k, m = map(int, input().split())
    line = [int(input().strip()) for _ in range(k)]
    line.sort()
    solution()