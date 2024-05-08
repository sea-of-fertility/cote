from collections import deque


def solution():
    answer = {x: 0}
    de = deque([x])

    while de:
        item = de.popleft()
        if answer[item] < k:
            for i in graph[item]:
                if i not in answer:
                    answer[i] = answer[item] + 1
                    de.append(i)
    return answer


if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)

    dic = solution()
    answer = []
    for index, value in dic.items():
        if value == k:
            answer.append(index)
    answer.sort()
    if answer:
        for i in answer:
            print(i)
    else:
        print(-1)

"""4 4 2 1
1 2
1 3
2 3
2 4"""