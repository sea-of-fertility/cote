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
            new_weight = weight + value
            if new_weight < distance[new_node]:
                distance[new_node] = new_weight
                heapq.heappush(heap, (new_weight, new_node))

    return distance[destination]


if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    v1, v2 = map(int, input().split())

    path1 = solution(1, v1) + solution(v1, v2) + solution(v2, n)
    path2 = solution(1, v2) + solution(v2, v1) + solution(v1, n)
    answer = min(path1, path2)

    print(answer) if answer < INF else print(-1)
