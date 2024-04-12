import sys
from collections import deque

input = sys.stdin.readline


def solution():
    a, b = map(int, input().split())
    answer = 0
    numbers = deque(i+1 for i in range(a))
    targets = deque(map(int, input().split()))
    while targets:
        target = targets.popleft()
        index = numbers.index(target)
        case2 = index
        case3 = len(numbers) - index
        if case3 < case2:
            for _ in range(case3):
                numbers.appendleft(numbers.pop())
                answer += 1
        else:
            for _ in range(case2):
                numbers.append(numbers.popleft())
                answer += 1
        numbers.popleft()
    print(answer)


if __name__ == "__main__":
    solution()
