from collections import deque


def dfs(v, graph, answer):
    answer.append(v)
    for w in graph[v]:
        if w not in answer:
            answer = dfs(w, graph, answer)
    return answer


def bfs(v, graph):
    answer = [v]
    que = deque([v])

    while que:
        v = que.popleft()
        for w in graph[v]:
            if w not in answer:
                answer.append(w)
                que.append(w)
    return answer


def solution():
    n, m, v = map(int, input().split())
    graph = [[] for i in range(n+1)]
    answer = []
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, n+1):
        graph[i].sort()

    df = dfs(v, graph, answer)
    bf = bfs(v, graph)

    for i in df:
        print(i, end=" ")
    print()
    for i in bf:
        print(i, end=" ")


if __name__ == "__main__":
    solution()