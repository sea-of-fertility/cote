def solution(dp_tables, page_datas, n):
    for row, datas in enumerate(page_datas, start=1):
        for col in range(n+1):
            days = datas[0]
            pages = datas[1]
            if col - days < 0:
                dp_tables[row][col] = dp_tables[row-1][col]
            else:
                dp_tables[row][col] = max(dp_tables[row-1][col], dp_tables[row-1][col-days] + pages)
    print(dp_tables[-1][-1])


def main():
    n, k = map(int, input().split())
    page_datas = [list(map(int, input().split())) for _ in range(k)]
    dp_tables = [[0 for _ in range(n+1)] for _ in range(k+1)]
    solution(dp_tables, page_datas, n)


if __name__ == "__main__":
    main()