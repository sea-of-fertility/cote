import sys

input = sys.stdin.readline


def find_per(game, win):
    return int((win / game) * 100)


def solution():
    end = int(1e9)
    start = 1
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        new_per = find_per(x + mid, y + mid)
        if cur_per < new_per:
            end = mid - 1
            answer = mid

        else:
            start = mid + 1

    return answer


if __name__ == "__main__":
    x, y = map(int, input().split())
    cur_per = find_per(x, y)
    print(solution())

