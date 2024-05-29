import sys
input = sys.stdin.readline



def solution():
    end = int(1e9)
    start = 0
    while start <= end:
        mid = (start + end) // 2
        n = (mid + 1) * mid // 2
        if n > target:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        target = int(input())
        solution()
