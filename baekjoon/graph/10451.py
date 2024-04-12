import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v, visit, graph):
    visit[v] = True
    if not visit[graph[v]]:
        dfs(graph[v], visit, graph)


def solution():
    t = int(input())
    for _ in range(t):
        arr_len = int(input())
        maps = list(map(int, input().split()))
        maps.insert(0, 0)

        visit = [False] * (arr_len + 1)
        answer = 0

        for i in range(1, arr_len + 1):
            if not visit[i]:
                dfs(i, visit, maps)
                answer += 1

        print(answer)


if __name__ == "__main__":
    solution()
