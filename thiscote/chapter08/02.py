from collections import deque


def dfs(target):
    de = deque([1])
    while de:
        x = de.popleft()

        case = [x * 2, x * 3, x * 5, x + 1]

        for i in case:
            if i == target:
                return data[x] + 1

            elif 1 < i < value and data[i] == -1:
                data[i] = data[x] + 1
                de.append(i)


def solution(target):
    answer = dfs(target)
    print(answer)


if __name__ == "__main__":
    value = int(input())
    data = [-1 for i in range(value + 1)]
    data[1] = 0
    solution(value)
