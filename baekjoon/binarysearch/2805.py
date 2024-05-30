import sys

input = sys.stdin.readline

"""
리스트 컴프리헨션은 c로 구현되어있어서 python 코드보다 빠르다.

"""
def findCut(num):
    return sum(item - num for item in arr if item > num)


def binarySearch():
    start = 0
    end = arr[-1]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        find = findCut(mid)
        if find >= m:
            answer = mid
            start = mid - 1
        else:
            end = mid - 1
    print(answer)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    binarySearch()
