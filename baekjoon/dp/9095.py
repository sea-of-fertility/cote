

arr = [0 for _ in range(12)]

arr[1] = 1
arr[2] = 2
arr[3] = 4
arr[4] = 7


def solution(n):
    for item in range(5, n+1):
        arr[item] = arr[item-1] + arr[item-2] + arr[item-3]
    print(arr[n])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        data = int(input())
        solution(data) if data > 4 else print(arr[data])