def solution(n: int):
    answer = 0
    lenght = 1
    for i in range(n // 2):
        if i == 0:
            answer = arr[i][len(arr) // 2] + arr[-1][len(arr) // 2]
            lenght += 2
        for l in range(lenght):
            answer += arr[i][(len(arr) // 2) - i]

    answer += sum(arr[n // 2])


if __name__ == '__main__':
    t = int(input())
    for cnt in range(t):
        arr = list()
        n = int(input())
        for maps in range(n):
            arr = list(input().split())
        print(arr)
        print(f"#{cnt + 1} {arr[0]}") if n == 1 else print(f"#{cnt + 1} {solution(n)}")
