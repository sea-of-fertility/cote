import sys

input = sys.stdin.readline


def solution():
    number = int(input())

    dp_list = [0 for _ in range(number+1)]
    answer_list = [number]
    for i in range(1, number+1):

        if i <= 1:
            dp_list[i] = 0
        elif i <= 3:
            dp_list[i] = 1

        else:
            cnt = dp_list[i-1]
            if i%2==0 and cnt > dp_list[i//2]:
                cnt = dp_list[i // 2]
            if i%3==0 and cnt > dp_list[i//3]:
                cnt = dp_list[i//3]
            dp_list[i] = cnt + 1

    target = number
    while target != 1:
        find_min = {target - 1: dp_list[target - 1]}
        if target % 2 == 0:
            find_min[target//2] = dp_list[target//2]
        if target % 3 == 0:
            find_min[target//3] = dp_list[target//3]
        min_value = min(find_min.values())
        for key, value in find_min.items():
            if value == min_value:
                target = key
                answer_list.append(target)
                break

    print(dp_list[number])
    for i in answer_list:
        print(i, end=" ")


if __name__ == "__main__":
    solution()