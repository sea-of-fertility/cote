import sys
from collections import deque


def function(functions, number_list, length):
    for f in functions:
        if f == 'D':
            if length > 0:
                number_list.popleft()
                length -= 1
            else:
                print("error")
                return
        elif f == 'R':
            number_list.reverse()
    print(f"[{','.join(map(str, number_list))}]")


def solution():
    function_orders = deque(input())
    length = int(input())
    number_list = deque(input())
    n_l = deque()
    for item in number_list:
        if item.isdigit():
            n_l.append(int(item))
    function(function_orders, n_l, length)


def main():
    test = int(input())
    for _ in range(test):
        solution()


if __name__ == "__main__":
    main()
