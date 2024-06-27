import sys

input = sys.stdin.readline

max_value = -99


def solution():
    len_arr = len(arr)
    for index in range(len_arr-2):
        sum_value = arr[index]
        target = index + 1
        end = len_arr
        for item in range(target, len_arr-1):
            start = item + 1
            sum_value += arr[item]
            while item <= end:
                mid = (start + end) // 2



if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dic = {item: True for item in arr}
    arr.sort()

    solution()



