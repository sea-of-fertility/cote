def solution(n, L, J):
    dp_table = [[0 for _ in range(101)] for _ in range(n+1)]
    for row, weight in enumerate(L, start=1):
        for col in range(101):
            if col - weight < 0:
                dp_table[row][col] = dp_table[row-1][col]
            else:
                dp_table[row][col] = max(dp_table[row-1][col], dp_table[row-1][col-weight] + J[row-1])
    print(dp_table[-1][-2])


def main():
    n = int(input())
    L = list(map(int, input().split()))
    J = list(map(int, input().split()))
    solution(n, L, J)


if __name__ == "__main__":
    main()