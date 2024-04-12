def answer():
    for row in range(5):
        arr = input()
        arr = arr.split()
        print(arr)


def solution():
    cnt = int(input())
    for i in range(cnt):
        answer()


if __name__ == "__main__":
    solution()
