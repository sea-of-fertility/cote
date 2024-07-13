import sys

input = sys.stdin.readline

dic = dict()


def check(arr):
    for time in range(arr[0], arr[1]):
        if time in dic:
            return False
    return True


def setFalse(arr):
    for time in range(arr[0], arr[1]):
        dic[time] = False


def solution(arr):
    result = 0
    for lecture in arr:
        if check(lecture):
            result += 1
            setFalse(lecture)
    print(result)


def init():
    cnt = int(input())
    lecture_time = [list(map(int, input().split())) for _ in range(cnt)]
    lecture_time.sort(key=lambda x: (x[1] - x[0], x[0]))
    solution(lecture_time)


if __name__ == "__main__":
    init()