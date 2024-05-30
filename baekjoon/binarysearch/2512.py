import sys

input = sys.stdin.readline


def find_price(num):
    return sum(min(item, num) for item in local)


def solution():
    end = local[-1]
    start = 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        find = find_price(mid)
        if find <= m:

            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)


if __name__ == "__main__":
    n = int(input())
    local = list(map(int, input().split()))
    m = int(input())
    local.sort()

    print(local[-1]) if sum(local) <= m else solution()

