import sys

input = sys.stdin.readline


def solution(arr):
    result = 0
    end = 0
    for lecture in arr:
        if end <= lecture[0]:
            end = lecture[1]
            result += 1
    print(result)


def init():
    cnt = int(input())
    lecture_time = [list(map(int, input().split())) for _ in range(cnt)]
    lecture_time.sort(key=lambda x: (x[1], x[0]))
    solution(lecture_time)


if __name__ == "__main__":
    init()
