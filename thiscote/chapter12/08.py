import sys

input = sys.stdin.readline


def solution():
    num = 0
    strings = []

    for item in arr:
        if item.isdigit():
            num += int(item)
        else:
            strings.append(item)

    strings.sort()
    strings = "".join(strings)
    strings += str(num)
    return strings


if __name__ == "__main__":
    arr = list(input().strip())
    print(solution())
