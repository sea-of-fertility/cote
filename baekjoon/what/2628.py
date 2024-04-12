import sys

input = sys.stdin.readline


def solution():
    row, col = map(int, input().split())
    row_cut_list = [0, col]
    col_cut_list = [0, row]
    cnt = int(input())
    for _ in range(cnt):
        cnt = list(map(int, input().split()))
        row_cut_list.append(cnt[1]) if cnt[0] == 0 else col_cut_list.append(cnt[1])

    row_cut_list.sort()
    col_cut_list.sort()

    big_size = 0
    for i in range(1, len(row_cut_list)):
        big_size = row_cut_list[i] - row_cut_list[i-1] if row_cut_list[i] - row_cut_list[i-1] > big_size else big_size
    answer = big_size
    big_size = 0
    for i in range(1, len(col_cut_list)):
        big_size = col_cut_list[i] - col_cut_list[i-1] if col_cut_list[i] - col_cut_list[i-1] > big_size else big_size

    print(answer * big_size)


if __name__ == "__main__":
    solution()
    list(map(int, input().split()))
