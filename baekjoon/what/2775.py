import sys

input = sys.stdin.readline


def solution():
    t = int(input().strip())
    for i in range(t):
        house = [[]]
        k = int(input().strip())
        n = int(input().strip())
        house = [[0]*n] * (k+1)
        house[0] = [base for base in range(1, n+1)]
        for floor in range(1, k+1):
            for ho in range(n):
                if ho == 0:
                    house[floor][0] = 1
                else:
                    house[floor][ho] = house[floor-1][ho] + house[floor][ho-1]
        print(house[-1][-1])


if __name__ == "__main__":
    solution()

