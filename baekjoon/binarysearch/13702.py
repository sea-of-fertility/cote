import sys

input = sys.stdin.readline


def find_cup(mid):
    return sum(i // mid for i in arr)


def solution():
    end = arr[-1]
    start = 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cup = find_cup(mid)

        if cup >= k:
            start = mid + 1
            answer = mid

        else:
            end = mid - 1

    return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = sorted([int(input()) for _ in range(n)])
    print(solution())
