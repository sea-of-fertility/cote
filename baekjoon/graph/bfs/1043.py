import sys
from collections import deque


input = sys.stdin.readline


def bfs():
    de = deque(true_people)
    while de:
        popleft = de.popleft()
        if not peoples[popleft]:
            peoples[popleft] = True
            for node in graph[popleft]:
                de.append(node)


def solution():
    bfs()
    fact_knowers = {}
    for index, item in enumerate(peoples):
        if item:
            fact_knowers[index] = True
    return fact_knowers


if __name__ == "__main__":
    n, m = map(int, input().split())
    answer = m
    graph = [[] for _ in range(n+1)]
    true_people = list(map(int, input().split()))[1:]
    peoples = [False for _ in range(n+1)]
    party_list = []

    for _ in range(m):
        party_peoples = list(map(int, input().split()))[1:]
        party_list.append(party_peoples)
        for start in party_peoples:
            for end in party_peoples:
                if start == end:
                    continue
                graph[start].append(end)


    fact_knowers = solution()
    for party in party_list:
        for p in party:
            if p in fact_knowers and fact_knowers[p]:
                answer -= 1
                break
    print(answer)
