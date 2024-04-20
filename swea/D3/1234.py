from collections import deque


def solution():
    while arr:
        popleft = arr.popleft()
        if answer and answer[-1] == popleft:
            answer.pop()
        else:
            answer.append(popleft)


if __name__ == '__main__':
    for i in range(10):
        answer = deque()
        n, arr = input().split()
        arr = deque(arr)

        answer.append(arr.popleft())
        solution()
        answer = "".join(answer)
        print(f"#{i+1} {answer}")
