import sys


input = sys.stdin.readline


def two_pointer():
    global answer
    start = 0
    end = n-1

    while start < end:
        value = arr[start] + arr[end]
        if value < target:
            start += 1

        elif value > target:
            end -= 1
        else:
            start += 1
            end -= 1
            answer += 1


if __name__ == "__main__":
    answer = 0
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    target = int(input())
    two_pointer()
    print(answer)
