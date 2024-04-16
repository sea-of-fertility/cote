def solution():
    for i in range(n):
        arr[-1] -= 1
        arr[0] += 1
        arr.sort()
    return arr[-1] - arr[0]


if __name__ == '__main__':
    for cnt in range(10):
        n = int(input())
        arr = list(map(int, input().split()))
        print(f"#{cnt+1} {solution()}")