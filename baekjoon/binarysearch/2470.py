import sys

input = sys.stdin.readline


def find_quantity(length):
    return sum(item // length for item in arr)


def binary():
    start = 1
    end = arr[-1]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        quantity = find_quantity(mid)

        if m <= quantity:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    binary1 = binary()
    print(binary1)
