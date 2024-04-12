from _collections import deque


def solution():
    n = int(input())
    answer = deque(i for i in range(1, n+1))
    if n <= 2:
        return n

    while len(answer) != 0:
        answer.popleft()

        if len(answer) == 1:
            return answer[0]
        bottom = answer.popleft()
        answer.append(bottom)


if __name__ == '__main__':
    print(solution())