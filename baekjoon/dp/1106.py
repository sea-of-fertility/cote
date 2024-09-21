INF = int(1e7)


def init(c, n):
    dp_tables = [[INF for _ in range(c+1)] for _ in range(n+1)]
    dp_tables[0][0] = 0
    return dp_tables


def solution(c, n, cites):
    dp_tables = init(c, n)

    for row, arr in enumerate(cites, start=1):
        price = arr[0]
        people = arr[1]
        for col in range(c+1):
            if col - people < 0:
                dp_tables[row][col] = min(price, dp_tables[row-1][col])
            else:
                dp_tables[row][col] = min(dp_tables[row][col-people] + price, dp_tables[row-1][col])
    print(dp_tables[-1][-1])


def main():
    c, n = map(int, input().split())
    cites = [list(map(int, input().split())) for _ in range(n)]
    solution(c, n, cites)


if __name__ == "__main__":
    main()
