import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline


def solution(start, destination):
    distance = [INF for _ in range(n + 1)]
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)

        if distance[node] < weight:
            continue

        for value, new_node in graph[node]:
            value += weight
            if value < distance[new_node]:
                distance[new_node] = value
                heapq.heappush(heap, (value, new_node))

    return distance[destination]


if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph[b].append([c, a])
    v1, v2 = map(int, input().split())

    answer = solution(1, v1) + solution(v2, n) + solution(v1, v2)
    print(answer) if answer < INF else print(-1)
