def solution():
    dic = {}
    num = [0 for _ in range(k+1)]
    for item in arr:
        num[item] += 1

    for index, value in enumerate(num):
        if value != 0:
            pass

    return num[k]


if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(f"#{i+1} {solution()}")
