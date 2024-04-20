def solution():
    for item in arr:
        if item not in dic.keys():
            dic[item] = 1
        else:
            dic[item] += 1

    for key, item in dic.items():
        if item == 1 or item == 3:
            return key


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        dic = {}
        arr = list(map(int, input().split()))
        print(f"#{i+1} {solution()}")