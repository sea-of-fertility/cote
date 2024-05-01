import sys

input = sys.stdin.readline


def solution():
    for item in data:
        if save[-1] == item:
            continue
        else:
            save.append(item)


if __name__ == "__main__":
    data = list(input().strip())
    save = [data[0]]
    data = data[1:]
    solution()
    print(min(save.count('1'), save.count('0')))
