import heapq
import sys

INF = sys.maxsize


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start][start] = 0
    while heap:
        weight, nodeNumber = heapq.heappop(heap)

        if distance[start][nodeNumber] < weight:
            continue

        for value, node in graph[nodeNumber]:
            value = value + weight
            if value < distance[start][node]:
                distance[start][node] = value
                heapq.heappush(heap, (value, node))


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    answer = []
    graph = [[] for _ in range(n + 1)]
    distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])

    for member in range(1, n + 1):
        dijkstra(member)

    answer = 0
    for index in range(len(distance[x])):
        new_weight = distance[x][index] + distance[index][x]
        answer = max(new_weight, answer) if new_weight < INF else answer

    print(answer)
