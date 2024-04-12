import sys

input = sys.stdin.readline


def solution():
    number = int(input())
    numbers = [0 for _ in range(number + 1)]
    d = [0 for _ in range(number + 1)]
    for i in range(2, number+1):
        if 2 <= i <= 3:
            numbers[i] = 1
        else:
            numbers[i] = numbers[i-1] + 1
            if i % 2 == 0 and numbers[i] > numbers[i//2] + 1:
                numbers[i] = numbers[i//2] + 1
            if i % 3 == 0 and numbers[i] > numbers[i//3] + 1:
                numbers[i] = numbers[i // 3] + 1
    print(numbers[number])


if __name__ == '__main__':
    solution()