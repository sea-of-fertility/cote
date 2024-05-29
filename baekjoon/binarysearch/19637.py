import sys
input = sys.stdin.readline


def solution(start, end, target, result):
    while start <= end:
        mid = (start + end) // 2
        if target < title[mid]:
            end = mid-1
            result = title[mid]
        elif target == title[mid]:
            return title_dict[target]
        elif title[mid] < target:
            start = mid + 1

    return title_dict[result]


if __name__ == "__main__":
    n, m = map(int, input().split())
    title_dict = {}
    answer_dict = {}
    for _ in range(n):
        name, value = input().split()
        if int(value) not in title_dict:
            title_dict[int(value)] = name
    title = [item for item in title_dict.keys()]
    title.sort()
    data = set()
    for _ in range(m):
        data = int(input())
        if data not in answer_dict:
            print(solution(0, len(title)-1, data, title[-1]))
        else:
            print(answer_dict[data])