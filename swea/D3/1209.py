def solution():
    answer = 0
    for cnt in range(100):
        sum_arr = sum(arr[cnt])
        answer = sum_arr if answer < sum_arr else answer

    move = 0
    cross = 0
    for cnt in range(100):
        cross += arr[cnt][move]
        move += 1

    answer = cross if answer < cross else answer

    move = 0
    cross = 0
    for cnt in range(99, -1, -1):
        cross += arr[cnt][move]
        move += 1
    answer = cross if answer < cross else answer


    for i in range(1, 100):
        for j in range(100):
            arr[i][j] += arr[i-1][j]

    sum_arr = max(arr[99])
    answer = sum_arr if answer < sum_arr else answer
    return answer


if __name__ == '__main__':
    for i in range(10):
        arr = []
        input()
        for _ in range(100):
            arr.append(list(map(int, input().split())))
        print(f"#{i+1} {solution()}")
