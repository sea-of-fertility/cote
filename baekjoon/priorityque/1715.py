import sys
import heapq

input = sys.stdin.readline


def solution():
    heapq.heapify(arr)
    answer = 0
    poket = heapq.heappop(arr)
    while len(arr) > 0:
        if poket != 0:
            heappop = heapq.heappop(arr)
            process = poket + heappop
            heapq.heappush(arr, process)
            answer += process
            poket = 0
        else:
            poket = heapq.heappop(arr)
    return  answer


if __name__ == "__main__":
    n = int(input())
    arr = [int(input().strip()) for _ in range(n)]

    print(solution())
