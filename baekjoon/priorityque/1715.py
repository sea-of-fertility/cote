import sys
import heapq

input = sys.stdin.readline


def solution():
    heapq.heapify(arr)
    result = 0

    while len(arr) > 1:
        one = heapq.heappop(arr)
        two = heapq.heappop(arr)
        result += one + two
        heapq.heappush(arr, one + two)
    print(result)


if __name__ == "__main__":
    n = int(input())
    arr = [int(input().strip()) for _ in range(n)]
    solution()
