import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1]


def solution():
    for x in range(1, row):
        for y in range(col):
            max_item = 0
            for move in dy:
                if 0 < y + move < col:
                    back_item = arr[y + move][x-1]
                    if max_item < back_item:
                        max_item = back_item
            arr[y][x] += max_item


if __name__ == "__main__":
    test_case = int(input())

    for test in range(test_case):
        col, row = map(int, input().split())
        arr = [[0 for _ in range(row)] for _ in range(col)]
        data = deque(map(int, input().split()))
        for i in range(col):
            for j in range(row):
                arr[i][j] = data.popleft()
        solution()
        answer = 0
        for find in range(col):
            if answer < arr[find][-1]:
                answer = arr[find][-1]

        print(answer)

    """
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
    """
