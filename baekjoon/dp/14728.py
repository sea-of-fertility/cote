def solution(datas, t):
    dp_tables = [[0 for _ in range(t+1)] for _ in range(len(datas)+1)]
    for row, data in enumerate(datas, start=1):
        k = data[0]
        s = data[1]
        for col in range(t+1):
            if col - k < 0:
                dp_tables[row][col] = dp_tables[row-1][col]
            else:
                dp_tables[row][col] = max(dp_tables[row-1][col], dp_tables[row-1][col-k] + s)
    print(dp_tables[-1][-1])


def main():
    n, t = map(int, input().split())
    datas = [list(map(int, input().split())) for _ in range(n)]
    solution(datas, t)


if __name__ == "__main__":
    main()