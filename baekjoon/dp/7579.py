import sys


input = sys.stdin.readline


def back_snap(row, col, app, mem):
    weight = app[0]
    value = app[1]
    if col - value < 0:
        return mem[row-1][col]
    else:

        return max(mem[row-1][col], mem[row-1][col-value] + weight)


def solution(arr, mem, k):
    answer = int(1e7)
    for row, app in enumerate(arr):
        for col in range(len(mem[0])):
            mem[row+1][col] = back_snap(row + 1, col, app, mem)
            if mem[row+1][col] >= k:
                answer = min(answer, col)
    print(answer)


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mem = [[0 for _ in range(sum(c)+1)] for _ in range(n + 1)]
    arr = list(zip(a, c))
    solution(arr, mem, k)


if __name__ == "__main__":
    main()
