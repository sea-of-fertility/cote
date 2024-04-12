
def answer(std):
    group = std // 3
    if group > 1:
        return group
    elif std >= 3:
        return 1
    else:
        return 0


def solution():
    cnt = int(input())
    for i in range(cnt):
        student = int(input())
        print(f"#{i + 1} {answer(student)}")


if __name__ == "__main__":
    solution()