import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    if start > end:
        print("no")
        return

    mid = end+start//2

    if item_list[mid] == target:
        print("yes")
        return
    elif item_list[mid] > target:
        return binary_search(target, start, mid - 1)

    else:
        return binary_search(target, mid + 1, end)


if __name__ == "__main__":
    n = int(input())
    item_list = list(map(int, input().split()))
    item_list.sort()
    m = int(input())
    order_list = list(map(int, input().split()))
    for order in order_list:
        binary_search(order, 0, len(item_list)-1)


"""
5
8 3 7 9 2
3
5 7 9
"""