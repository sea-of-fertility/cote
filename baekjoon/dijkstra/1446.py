import sys
import heapq


INF = sys.maxsize



def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        node, weight = heapq.heappop(heap)
        print(node, weight)
        if distance[node] < weight:
            continue

        for des, w in graph[node]:
            total_distance = w + weight
            if total_distance < distance[des]:
                distance[des] = total_distance
                heapq.heappush(heap, (des, total_distance))


if __name__ == "__main__":
    n, d = map(int, input().split())
    graph = [[] for _ in range(d+1)]
    distance = [weight for weight in range(d+1)]
    for _ in range(n):
        start, end, weight = map(int, input().split())
        if start <= d and end < d:
            graph[start].append([end, weight])
    dijkstra()
    print(distance[d])