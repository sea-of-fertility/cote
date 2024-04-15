def binary_search(arr, start, end):

    if start > end:
        return -1

    item = (start + end) // 2

    if target == arr[item]:
        print("success")
        return item
    elif target < arr[item]:
        return binary_search(arr, start, item-1)
    else:
        return binary_search(arr, item + 1, end)


def solution(arr):
    search = binary_search(arr, 0, len(arr))
    print(search)


if __name__ == "__main__":
    cnt = 0
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    solution(array)
