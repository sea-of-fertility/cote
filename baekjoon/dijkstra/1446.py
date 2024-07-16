import sys
import heapq

INF = sys.maxsize


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        weight, node = heapq.heappop(heap)
        if distance[node] < weight:
            continue

        for index, w in enumerate(graph[node]):
            total_distance = w + weight
            if total_distance < distance[index]:
                distance[index] = total_distance
                heapq.heappush(heap, (total_distance, index))


if __name__ == "__main__":
    n, d = map(int, input().split())
    graph = [[INF for _ in range(d + 1)] for _ in range(d + 1)]
    distance = [INF for _ in range(d + 1)]
    for row in range(d + 1):
        for col in range(d + 1):
            if col - row >= 0:
                graph[row][col] = col - row

    for _ in range(n):
        start, end, weight = map(int, input().split())
        if start <= d and end <= d:
            graph[start][end] = min(graph[start][end], weight)

    dijkstra()
    print(distance[d])
