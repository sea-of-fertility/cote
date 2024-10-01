import sys

input = sys.stdin.readline
INF = sys.maxsize


def main():
    d, p = map(int, input().split())
    dp_tables = [0 for _ in range(d+1)]
    dp_tables[0] = INF
    for _ in range(p):
        l, c = map(int, input().split())
        copy_tables = dp_tables.copy()
        for index in range(l, d+1):
            if dp_tables[index-l]:
                dp_tables[index] = max(dp_tables[index], min(copy_tables[index-l], c))
    print(dp_tables[-1])


if __name__ == "__main__":
    main()