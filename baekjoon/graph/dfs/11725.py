import sys
from collections import deque


input = sys.stdin.readline


def dfs():
    de = deque([1])
    while de:
        pop_item = de.pop()
        for item in graph[pop_item]:
            if not visit[item]:
                answer[item] = pop_item
                visit[item] = True
                de.append(item)


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    answer = [0 for _ in range(n+1)]
    visit = [False for _ in range(n+1)]
    for _ in range(n-1):
        stat, end = map(int, input().split())
        graph[stat].append(end)
        graph[end].append(stat)
    dfs()
    for index in range(2, n+1):
        print(answer[index])
