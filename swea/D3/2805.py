def solution():
    answer = sum(arr[n//2])
    start = n // 2
    length = 1

    for i in range(n // 2):
        answer += sum(arr[i][start:start + length])
        answer += sum(arr[-(i+1)][start:start + length])

        start -= 1
        length += 2

    return answer


if __name__ == '__main__':
    t = int(input())
    for cnt in range(t):
        arr = list()
        n = int(input())
        for maps in range(n):
            arr.append(list(map(int, input().strip())))
        print(f"#{cnt + 1} {sum(arr[0])}") if n == 1 else print(f"#{cnt + 1} {solution()}")
